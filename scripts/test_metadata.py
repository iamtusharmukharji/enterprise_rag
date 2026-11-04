from app.ingestion.loader import load_documents
from app.ingestion.metadata import extract_metadata


documents = load_documents("documents")

metadata, content = extract_metadata(documents[0]["content"])

print("METADATA")
print(metadata)

print("\nCONTENT")
print(content[:1000])