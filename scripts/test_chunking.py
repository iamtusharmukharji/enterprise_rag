from app.ingestion.loader import load_documents
from app.ingestion.chunker import chunk_document


documents = load_documents("documents")

all_chunks = []

for document in documents:
    chunks = chunk_document(document)
    all_chunks.extend(chunks)


print(f"Documents: {len(documents)}")
print(f"Chunks: {len(all_chunks)}")


for chunk in all_chunks[:10]:
    print("\n" + "=" * 100)

    # print("CHUNK ID:")
    # print(chunk["metadata"]["chunk_id"])

    # print("\nSOURCE:")
    # print(chunk["metadata"]["source"])

    # print("\nCONTENT:")
    # print(chunk["content"])
    print(chunk)