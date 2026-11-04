from app.rag.generator import generate_answer
from scripts.test_hybrid_retrieval import results, query
# Keep your existing hybrid retrieval and reranking code.
# `results` should contain the top 5 reranked chunks.



response = generate_answer(
    question=query,
    documents=results,
)

print("\nPROMPT:")
print(query)

print("\nANSWER:")
print(response["answer"])

print("\nSOURCES:")
for source in response["sources"]:
    print(source)