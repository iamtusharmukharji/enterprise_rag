from collections import defaultdict

from app.retrieval.dense_retriever import dense_search


def reciprocal_rank_fusion(
    ranked_lists: list[list[dict]],
    top_k: int = 5,
    rrf_k: int = 60,
) -> list[dict]:
    
    fused_scores = defaultdict(float)
    documents = {}

    for results in ranked_lists:
        for rank, result in enumerate(results, start=1):
            chunk_id = result.get("chunk_id")

            if not chunk_id:
                continue

            fused_scores[chunk_id] += 1 / (rrf_k + rank)
            documents[chunk_id] = result

    ranked_ids = sorted(
        fused_scores,
        key=fused_scores.get,
        reverse=True,
    )[:top_k]

    return [
        {
            **documents[chunk_id],
            "rrf_score": fused_scores[chunk_id],
        }
        for chunk_id in ranked_ids
    ]


def hybrid_search(
    query: str,
    bm25_retriever,
    top_k: int = 5,
    candidate_k: int = 10,
) -> list[dict]:
    dense_results = dense_search(query, top_k=candidate_k)
    sparse_results = bm25_retriever.search(query, top_k=candidate_k)

    return reciprocal_rank_fusion(
        [dense_results, sparse_results],
        top_k=top_k,
    )