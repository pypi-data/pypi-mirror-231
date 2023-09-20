"""Sentence embedding utilities"""
import numpy as np
from sentence_transformers import SentenceTransformer

sentence_model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-mpnet-base-v2").eval()


def sentence_embeddings(sentences: list[str], normalise: bool = True) -> np.ndarray:
    """
    Embed (english) text using a sentence transformer

    Parameters
    ----------
    sentences : list[str]
        Sentences to embed
    normalise : bool
        Normalise the embedding vector

    Returns
    -------
    np.ndarray
        2d embedding matrix, each row is a sentence embedding vector
    """
    v = sentence_model.encode(sentences, show_progress_bar=False)
    if normalise:
        return v / np.linalg.norm(v, axis=1)[:, np.newaxis]
    return v


def mean_max_similarity(embeddings_a: np.ndarray, embeddings_b: np.ndarray) -> float:
    """
    Given 2d text embedding matrices, calculate the mean max dot product of each row in A with rows in B.

    Parameters
    ----------
    embeddings_a : np.ndarray
        2d matrix where each row is a text embedding
    embeddigs_b : np.ndarray
        2d matrix where each row is a text embedding

    Returns
    -------
    float
        Average max dot product of rows in A with rows in B
    """
    return embeddings_a.dot(embeddings_b.T).max(axis=1).mean()
