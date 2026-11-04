from rank_bm25 import BM25Okapi


class BM25Retriever:
    def __init__(self, chunks: list[dict]):
        self.chunks = chunks

        self.tokenized_chunks = [chunk["content"].lower().split()
                                 for chunk in chunks]

        self.bm25 = BM25Okapi(self.tokenized_chunks)

    def search(self, query: str, top_k: int = 5) -> list[dict]:
        if not query.strip():
            raise ValueError("Query cannot be empty.")

        query_tokens = query.lower().split()
        scores = self.bm25.get_scores(query_tokens)

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda index: scores[index],
            reverse=True,
        )[:top_k]

        results = []

        for index in ranked_indices:
            chunk = self.chunks[index]

            results.append(
                {
                    **chunk,
                    "score": float(scores[index]),
                }
            )

        return results
