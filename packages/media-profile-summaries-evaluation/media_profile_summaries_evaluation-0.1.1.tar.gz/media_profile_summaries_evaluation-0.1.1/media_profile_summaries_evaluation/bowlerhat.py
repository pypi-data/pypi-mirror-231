"""Bowler Hat utilities"""
import requests
import re
import json
from typing import Union

import numpy as np
from media_profile_summaries_evaluation.models import BowlerHat, Entities


class Client:
    """
    Simple interface with Bowler Hat REST API

    Parameters
    ----------
    bh_url_base : str
        URL for Bowler Hat REST API
    snippet_pattern : str
        Expected format for individual snippets in evidence
    reference_pattern : str
        Expected format for references

    Attributes
    ----------
    bh_url_base : str
        URL for Bowler Hat REST API
    snippet_pattern : re.Pattern
        Expected format for individual snippets in evidence
    reference_pattern : re.Pattern
        Expected format for references
    """

    def __init__(
        self, bh_url_base: str = "http://localhost:2060/bowlerhat/", snippet_pattern: str = r"\[(?P<id>\d+)\] \((?P<date>.*?)\) (?P<text>.*)\n", reference_pattern: str = r"\[(?P<reference>\d+)\]"
    ):
        self.snippet_pattern = re.compile(snippet_pattern)
        exp_keys = ("id", "date", "text")
        if not all(k in self.snippet_pattern.groupindex for k in exp_keys):
            raise Exception(f"Expected {exp_keys} in snippet_pattern named groups, got {list(self.snippet_pattern.groupindex.keys())}")

        self.reference_pattern = re.compile(reference_pattern)
        if "reference" not in self.reference_pattern.groupindex:
            raise Exception("Expected 'reference' in reference_pattern named groups")

        self.bh_url_base = bh_url_base

    def __call__(self, action: str, url_params: dict, form_data: str) -> list:
        """
        Make a POST request to Bowler Hat API

        Parameters
        ----------
        action : str
            'batch' or otherwise (?)
        url_params : dict
            Query params
        form_data : str
            Body params

        Returns
        -------
        list
            Bowler Hat results
        """
        try:
            url = self.bh_url_base + action + "?" + "&".join([str(k) + "=" + str(v) for k, v in url_params.items()])
            res = requests.post(url, data=form_data.encode("utf-8"))
            if res.status_code == requests.codes.ok:
                if action == "batch":
                    results = res.text.split("\n")
                    return [json.loads(res) for res in results]
                return res.json()
            else:
                message = "Bowler Hat call failed with response: " + str(res.status_code)
                raise RuntimeError(message)
        except Exception as e:
            message = "Request to Bowler Hat errored: " + str(e)
            raise RuntimeError(message)

    def parse(self, text: str) -> BowlerHat:
        """
        Call Bowler Hat on a single text

        Parameters
        ----------
        text : str

        Returns
        -------
        BowlerHat
        """
        batch = [json.dumps({"data": [text], "params": {"regions": True}, "operations": ["entity", "text"]}, ensure_ascii=False)]
        results = self("batch", {}, "\n".join(batch))
        bh = BowlerHat.model_validate(results[0][0])
        bh.references = [int(m.group("reference")) for m in self.reference_pattern.finditer(text)]
        return bh

    def parse_from_snippets(self, text: str, combine: bool = True) -> Union[BowlerHat, list[BowlerHat]]:
        """
        Extract all entities from snippets.

        As a snippet may not be in English and date processing is not supported for non-English languages,
        we split the snippet according to `snippet_pattern` and process the date and text separately.
        i.e. "[1] (January 2020) Hola, amigo, que tal? De donde eres? Soy de Australia. Me llama Lewis. Como te llamas?" will be split
        into "January 2020" and "Hola, amigo, que tal? De donde eres? Soy de Australia. Me llama Lewis. Como te llamas?"

        Parameters
        ----------
        text : str
        combine : bool
            Combine results from individual snippets

        Returns
        -------
        Union[BowlerHat, list[BowlerHat]]
            Combined results or individual snippet results
        """
        results = []
        for m in self.snippet_pattern.finditer(text):
            res_published = self.parse("It is " + m.group("date"))
            res_snippet = self.parse(m.group("text"))
            res_snippet.id = int(m.group("id"))

            if not res_published.entities or not res_published.entities.datetime:
                raise Exception(f"Did not find published date in '{m.group(0)}' using '{self.snippet_pattern}'")

            if not res_snippet.entities:
                res_snippet.entities = Entities()

            if not res_snippet.entities.datetime:
                res_snippet.entities.datetime = []
            res_snippet.entities.datetime.extend(res_published.entities.datetime)
            results.append(res_snippet)

        if combine:
            result = {
                "document_language": {k: v for r in results for k, v in (r.document_language or {}).items()},
                "entities": {
                    "person": np.concatenate([r.entities.person or [] for r in results]),
                    "organisation": np.concatenate([r.entities.organisation or [] for r in results]),
                    "location": np.concatenate([r.entities.location or [] for r in results]),
                    "datetime": np.concatenate([r.entities.datetime or [] for r in results]),
                    "monetary_value": np.concatenate([r.entities.monetary_value or [] for r in results]),
                },
            }
            return BowlerHat.model_validate(result)
        return results
