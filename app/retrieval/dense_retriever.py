from app.embeddings.embedder import create_query_embedding
from app.vectorstore.qdrant import client, COLLECTION_NAME


def dense_search(query: str, top_k: int = 5) -> list[dict]:
    if not query.strip():
        raise ValueError("Query cannot be empty.")

    query_vector = create_query_embedding(query)

    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k,
        with_payload=True,
        with_vectors=False,
    )

    results = []

    for point in response.points:
        payload = point.payload or {}

        results.append({
            "chunk_id": payload.get("chunk_id"),
            "document_id": payload.get("document_id"),
            "content": payload.get("content"),
            "metadata": {
                key: value
                for key, value in payload.items()
                if key not in {"chunk_id", "document_id", "content"}
            },
            "score": point.score,
        })

    return results