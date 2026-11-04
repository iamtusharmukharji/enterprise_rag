from pydantic import BaseModel
from typing import List

class DocumentGrade(BaseModel):
    """
    Schema for grading document as per user's query
    """
    is_relevant : bool
    sources : List[dict]

class OptimisedQuery(BaseModel):
    """
    Sctructured schema for getting rewritten query from LLM with structured output
    """
    rewritten_query : str