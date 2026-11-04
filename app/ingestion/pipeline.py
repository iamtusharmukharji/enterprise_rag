
from app.ingestion.loader import load_documents
from app.ingestion.chunker import chunk_document
from app.retrieval.bm25_retriever import BM25Retriever

documents = load_documents('documents')

chunks = []
for data in documents:
    single_chunk = chunk_document(data)
    chunks.extend(single_chunk)

bm25_retriever = BM25Retriever(chunks)