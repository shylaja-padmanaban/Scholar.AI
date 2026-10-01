from backend.app.services.vector_store import (
    load_embeddings,
    build_faiss_index,
    search_faiss
)

from backend.app.services.embeddings_service import generate_embedding


stored_data = load_embeddings("backend/app/embeddings.json")

print("Number of chunks:", len(stored_data))


index = build_faiss_index(stored_data)

print("Vectors in FAISS:", index.ntotal)
print("Vector dimension:", index.d)


question = "What is robot locomotion?"

query_embedding = generate_embedding(question)


results = search_faiss(
    query_embedding,
    index,
    stored_data,
    top_k=3
)


print("\nTOP 3 RESULTS\n")

for result in results:
    print("Chunk ID:", result["chunk_id"])
    print("Score:", result["score"])
    print("Text:", result["text"][:500])
    print("=" * 60)