from sentence_transformers import SentenceTransformer
from typing import List

MODEL = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(text: str)->List[float]:
    """
    Generate embeddings for Node Text.

    Args:
        text (str): The input text to be embedded.
    """
    return MODEL.encode(text).tolist()

def similarity(vec1: List[float], vec2: List[float]) -> float:
    """
    Compute cosine similarity between two Node vectors.

    Args:
        vec1 (List[float]): The first Node vector.
        vec2 (List[float]): The second Node vector.
    """
    from numpy import dot
    from numpy.linalg import norm

    return dot(vec1, vec2) / (norm(vec1) * norm(vec2))