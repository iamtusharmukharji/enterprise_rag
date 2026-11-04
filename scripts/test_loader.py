from app.ingestion.loader import load_documents


documents = load_documents("documents")

print(f"Loaded documents: {len(documents)}")

for document in documents[:2]:
    print("=" * 80)
    print("METADATA:", document["metadata"])
    print(document["content"][:1000])