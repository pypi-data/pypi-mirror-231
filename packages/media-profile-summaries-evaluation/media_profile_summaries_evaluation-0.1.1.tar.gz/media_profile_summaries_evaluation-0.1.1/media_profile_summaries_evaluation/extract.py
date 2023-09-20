"""A set of functions for extracting various elements of interest from a given text"""
import logging
import re
from unidecode import unidecode
from datetime import datetime
from media_profile_summaries_evaluation.models import Entities

log = logging.getLogger(__name__)

TERMS = re.compile(r"((?:[A-Z][a-z]*)(?:[\s\-][A-Z][a-z]*)|(?:[$£€]\d+(?:\.\d+)?))\b")


def _year_month_day(date: str) -> tuple:
    """
    Extract the year, month and day from a given datestring.

    Parameters
    ----------
    date : str
        Bowler Hat formatted datestring

    Returns
    -------
    tuple
        year, month, day
    """
    year, month, day = None, None, None
    try:
        dt = datetime.strptime(date, "%Y")
        year = dt.year
    except Exception:
        try:
            dt = datetime.strptime(date, "%Y-%m")
            year, month = dt.year, dt.month
        except Exception:
            try:
                dt = datetime.strptime(date, "%Y-%m-%d")
                year, month, day = dt.year, dt.month, dt.day
            except Exception:
                log.exception("'Expected date of format YYYY, YYYY-mm, or YYYY-mm-dd")
    return year, month, day


def terms(text: str) -> set[str]:
    """
    Find capitalised terms, etc. in a given text.

    Parameters
    ----------
    text : str
        The text to search through

    Returns
    -------
    set[int]
        Terms of interest (lowercased)
    """
    toi = set()
    for match in TERMS.finditer(text):
        start, _ = match.span(0)
        value = match.group(0).strip()
        if any([c.isdigit() for c in value]) or (start > 2 and text[start - 2] != "." and text[start - 1] != "\n"):
            # NOTE: will throw away any toi at the start of a sentence.
            toi.add(value.lower())
    return toi


def people(entities: Entities, expand_for_last: bool = True) -> set[str]:
    """
    Extract peoples names from bowlerhat 'person' entities, possibly expanding to include last names.

    Parameters
    ----------
    entities : Entities
        Bowler Hat entities
    expand_for_last : bool
        Include last names on their own

    Returns
    -------
    set[str]
        Names
    """
    people_ = entities.person or []
    values = []
    for p in people_:
        values.append(p.value)
        if expand_for_last:
            values.append(p.value.rsplit(" ", 1)[-1])
    values = [unidecode(v.lower()) for v in values]
    return set(values)


def organisations(entities: Entities, expand_for_text: bool = True) -> set[str]:
    """
    Extract organisation names from bowlerhat 'organisation' entities, possibly expanding for the 'text' value as well as the 'value' value for each.

    Parameters
    ----------
    entities : Entities
        Bowler Hat entities
    expand_for_text : bool
        Include 'text' from each organisation

    Returns
    -------
    set[str]
        Organisations
    """
    orgs_ = entities.organisation or []
    values = []
    for o in orgs_:
        values.append(o.value)
        if expand_for_text:
            values.append(o.text)
    values = [unidecode(v.lower()) for v in values]
    return set(values)


def locations(entities: Entities, expand_for_regions: bool = True) -> set[str]:
    """
    Extract locations from bowlerhat 'location' entities, possibly expanding for the 'name' and 'country' in the 'regions' values.

    Parameters
    ----------
    entities : Entities
        Bowler Hat entities
    expand_for_regions : bool
        Include regions and countries of locations

    Returns
    -------
    set[str]
        Locations
    """
    locations_ = entities.location or []
    values = []
    for loc in locations_:
        values.append(loc.value)
        if expand_for_regions and loc.regions:
            for r in loc.regions:
                values.extend([r.name, r.country])
    values = [unidecode(v.lower()) for v in values]
    return set(values)


def dates(entities: Entities, expand_for_superdates: bool = True) -> set[str]:
    """
    Extract year, year-month and year-month-day datestrings from a set of bowlerhat datetime entities.

    Possibly expand the set to include the year and year-month when presented with a year-month or year-month-day datetime.

    Parameters
    ----------
    entities : Entities
        Bowler Hat formatted entities
    expand : bool
        Expand datetime to include super-datetimes (e.g. year and year-month if given year-month-day)

    Returns
    -------
    set[str]
        Standardised form of dates mentioned
    """
    datetimes = entities.datetime or []
    values = []
    for date in datetimes:
        y, m, d = _year_month_day(date.value)
        if expand_for_superdates:
            if y:
                values.append(str(y))
            if m:
                values.append(f"{y}-{m:02d}")
            if d:
                values.append(f"{y}-{m:02d}-{d:02}")
        else:
            if y and m and d:
                values.append(f"{y}-{m:02d}-{d:02}")
            elif y and m:
                values.append(f"{y}-{m:02d}")
            elif y:
                values.append(str(y))
    return set(values)


def monetaries(entities: Entities, *args) -> set[str]:
    """
    Extract monetary values as '{value} {currency}' from Bowler Hat entities

    Parameters
    ----------
    entities : Entities
        Bowler Hat entities

    Returns
    -------
    set[str]
        Monetary values
    """
    moneys = entities.monetary_value or []
    return set(f"{m.value} {m.currency}" for m in moneys)
