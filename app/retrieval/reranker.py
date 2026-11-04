from sentence_transformers import CrossEncoder

reranker_model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank_documents(
    query: str,
    documents: list[dict],
    top_k: int = 5,
) -> list[dict]:
    if not query.strip():
        raise ValueError("Query cannot be empty.")

    if not documents:
        return []

    pairs = [
        (query, document["content"])
        for document in documents
    ]

    scores = reranker_model.predict(pairs)

    ranked_documents = []

    for document, score in zip(documents, scores):
        ranked_documents.append({
            **document,
            "rerank_score": float(score),
        })

    ranked_documents.sort(
        key=lambda document: document["rerank_score"],
        reverse=True,
    )

    return ranked_documents[:top_k]