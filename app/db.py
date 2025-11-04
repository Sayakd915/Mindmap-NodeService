import os
from google.cloud import firestore
from app.config import GOOGLE_APPLICATION_CREDENTIALS

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

client = firestore.Client()

def save_node(node_data: dict) -> str:
    """
    Save a node to the database.

    Args:
        node_data (dict): The node data to save.
    """
    doc_ref = client.collection("nodes").document()
    doc_ref.set(node_data)
    return doc_ref.id

def get_all_nodes() -> list:
    """
    Get all nodes from the database.

    Returns:
        list: A list of nodes.
    """
    docs = client.collection("nodes").stream()
    return [{"id": doc.id, **doc.to_dict()} for doc in docs]

def get_node(node_id: str) -> dict:
    """
    Get a node from the database.

    Args:
        node_id (str): The ID of the node to get.
    """
    doc = client.collection("nodes").document(node_id).get()
    return {"id": doc.id, **doc.to_dict()} if doc.exists else None