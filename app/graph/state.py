from typing import TypedDict, Optional, List


class GraphState(TypedDict):

    question: str  # Original user question
    # Revised query when retrieval is insufficient
    rewritten_question: Optional[str]
    documents: List[dict] = []  # Retrieved and reranked chunks
    answer: Optional[str]  # Generated answer
    is_relevant: Optional[None | bool] = None  # Result of document relevance gradingy
    is_grounded: Optional[None | bool] = None  # Whether the answer is supported by context
    retry_count: int = 0  # Prevents unlimited retries
    sources: List[dict] = []  # Document and chunk references
    max_retries : int = 2
