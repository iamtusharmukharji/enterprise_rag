from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from uuid import uuid5, NAMESPACE_DNS

client = QdrantClient(
    url='http://localhost:6333'
)

COLLECTION_NAME = 'ent_rag'

if not client.collection_exists(COLLECTION_NAME):
    client.create_collection(
        collection_name = COLLECTION_NAME,
        vectors_config = VectorParams(size = 3072, distance = Distance.COSINE)
    )

def upsert_chunks(chunks: list[dict], vectors: list[list[float]]):

    points = []

    for chunk, vector in zip(chunks, vectors):
        metadata = chunk["metadata"]

        points.append(
            PointStruct(
                id=str(uuid5(NAMESPACE_DNS, metadata["chunk_id"])),
                vector = vector,
                payload = {
                    "content": chunk["content"],
                    **metadata
                }
            )
        )

    if points:
        client.upsert(
            collection_name = COLLECTION_NAME,
            points = points,
            wait = True,
        )





