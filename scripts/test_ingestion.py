
from app.ingestion.loader import load_documents
from app.ingestion.chunker import chunk_document
from app.embeddings.embedder import create_vector_embedding
from app.vectorstore.qdrant import upsert_chunks

documents = load_documents("documents")

chunks = []
for document in documents:
    chunks.extend(chunk_document(document))

texts = [chunk["content"] for chunk in chunks]
vectors = create_vector_embedding(texts)

inserted = upsert_chunks(chunks, vectors)

print(f"Chunks processed: {len(chunks)}")
print(f"Points upserted: {inserted}")
