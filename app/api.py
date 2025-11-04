from fastapi import APIRouter, HTTPException
from typing import List
from app.models import NodeCreate, NodeOut, SimilarNode
from app.db import save_node, get_all_nodes, get_node
from app.ml import get_embeddings, similarity
from datetime import datetime

router = APIRouter()

@router.post("/nodes", response_model=NodeOut)
def create_node(node: NodeCreate):
    embeddings = get_embeddings(node.title + " " + node.description)
    node_data = node.dict()
    node_data["created_at"] = datetime.now().isoformat()
    node_data["embedding"] = embeddings
    node_id = save_node(node_data)
    return NodeOut(id=node_id, **node_data)

@router.get("/nodes/{node_id}/similar", response_model=List[SimilarNode])
def find_similar_nodes(node_id: str, threshold: float = 0.7, top_k: int = 5):
    selected = get_node(node_id)
    if not selected:
        raise HTTPException(status_code=404, detail="Node not found")
    selected_emb = selected["embedding"]
    nodes = get_all_nodes()
    results = []
    for n in nodes:
        if n["id"] == node_id or "embedding" not in n:
            continue
        score = similarity(selected_emb, n["embedding"])
        if score >= threshold:
            results.append(SimilarNode(id=n["id"], title=n["title"], similarity=score))
    results.sort(key=lambda x: x.similarity, reverse=True)
    return results[:top_k]