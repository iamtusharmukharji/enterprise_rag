from pathlib import Path
from app.ingestion import metadata


def load_documents(documents_dir: str) -> list[dict]:
    documents = []

    for file_path in Path(documents_dir).rglob("*.md"):
        raw_content = file_path.read_text(encoding="utf-8")
        meta_data, content = metadata.extract_metadata(raw_content)
        meta_data['source'] = str(file_path)
        documents.append({
            "metadata": meta_data,
            "content": content,
        })

    return documents