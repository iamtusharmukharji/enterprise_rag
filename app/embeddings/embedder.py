from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.credentials import credentials

embedding_model = GoogleGenerativeAIEmbeddings(
        model= "models/gemini-embedding-001",
        google_api_key = credentials.gemini_api_key
)

def create_vector_embedding(chunk_list : list[str]) -> list[list[float]]:
    """Generate embeddings for multiple text chunks."""
    
    vector = embedding_model.embed_documents(chunk_list)

    return vector


def create_query_embedding(query: str) -> list[float]:
    """Generate an embedding for a user query."""
    if not query.strip():
        raise ValueError("Query cannot be empty.")

    return embedding_model.embed_query(query)

