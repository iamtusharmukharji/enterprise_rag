

def extract_metadata(content: str) -> tuple[dict, str]:
    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)

    if len(parts) != 3:
        return {}, content

    raw_metadata = parts[1].strip()
    document_content = parts[2].strip()

    metadata = {}

    for line in raw_metadata.splitlines():
        if ":" not in line:
            continue

        key, value = line.split(":", 1)

        metadata[key.strip()] = value.strip()

    return metadata, document_content