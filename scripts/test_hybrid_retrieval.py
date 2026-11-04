from app.retrieval.bm25_retriever import BM25Retriever
from app.retrieval.hybrid_retriever import hybrid_search
from app.ingestion.loader import load_documents
from app.ingestion.chunker import chunk_document
from app.retrieval.reranker import rerank_documents

# `chunks` = the same list produced by your ingestion pipeline.

documents = load_documents('documents')

chunks = []
for data in documents:
    single_chunk = chunk_document(data)
    chunks.extend(single_chunk)


bm25_retriever = BM25Retriever(chunks)

query = "Can you tell me the deployemnt policy?"

candidates = hybrid_search(
    query=query,
    bm25_retriever=bm25_retriever,
    top_k=10,
    candidate_k=20,
)

results = rerank_documents(
    query=query,
    documents=candidates,
    top_k=5,
)


if __name__ == "__main__":

    for rank, result in enumerate(results, start=1):
        print(
            f"\nRank: {rank}",
            f"\nDocument: {result['document_id']}",
            f"\nChunk: {result['chunk_id']}",
            f"\nRerank score: {result['rerank_score']:.4f}",
        )
        print(result["content"][:300])