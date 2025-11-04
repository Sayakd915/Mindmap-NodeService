from pydantic import BaseModel, Field
from typing import List, Optional

class NodeCreate(BaseModel):
    title: str
    description: str
    tags: Optional[List[str]] = []
    reminder: Optional[str]
    
class NodeOut(BaseModel):
    id: str
    title: str
    description: str
    tags: List[str]
    embedding: List[float]
    created_at: str
    
    
class SimilarNode(BaseModel):
    id: str
    title: str
    similarity: float