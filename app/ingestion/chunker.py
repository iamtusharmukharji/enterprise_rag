from langchain_text_splitters import RecursiveCharacterTextSplitter


splitter = RecursiveCharacterTextSplitter(
    chunk_size=900,
    chunk_overlap=100,
)


def chunk_document(document: dict) -> list[dict]:
    chunks = splitter.split_text(document["content"])

    results = []

    for index, chunk in enumerate(chunks):
        metadata = document["metadata"].copy()

        metadata["chunk_id"] = (
            f"{metadata['document_id']}_chunk_{index + 1:03d}"
        )

        results.append({
            "content": chunk,
            "metadata": metadata,
        })

    return results