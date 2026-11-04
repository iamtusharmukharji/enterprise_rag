
from app.ingestion.loader import load_documents
from app.ingestion.chunker import chunk_document
from app.embeddings.embedder import (
    create_vector_embedding,
    create_query_embedding,
)

documents = load_documents("documents")

chunks = []
for document in documents:
    chunks.extend(chunk_document(document))

texts = [chunk["content"] for chunk in chunks[:3]]

vectors = create_vector_embedding(texts)

print("Chunks:", len(texts))
print("Vectors:", len(vectors))
print("Dimensions:", len(vectors[0]))

query_vector = create_query_embedding(
    "How many working days of paternity leave are available?"
)

print("Query dimensions:", len(query_vector))

assert len(vectors) == len(texts)
assert len(query_vector) == len(vectors[0])
