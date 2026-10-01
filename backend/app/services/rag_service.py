from services.embeddings_service import generate_embedding
from services.vector_store import load_embeddings
from services.retrieval_service import search_similar_chunks
from services.llm_service import generate_answer


def answer_question(question):

    # 1. Convert question into embedding
    query_embedding = generate_embedding(question)

    # 2. Load stored embeddings
    stored_data = load_embeddings()

    # 3. Find the most relevant chunks
    results = search_similar_chunks(
        query_embedding,
        stored_data,
        top_k=3,
        threshold=0.5
    )

    # If no relevant chunks are found
    if not results:
        return "The information is not available in the provided research paper."

    # 4. Display retrieved chunks and similarity scores
    print("\n===== RETRIEVED CHUNKS =====")
    for i, result in enumerate(results):
        print(f"\n--- Chunk {i+1} ---")
        print(f"Chunk ID: {result.get('chunk_id')}")
        print(f"Score: {result['score']}")
        print(f"Page: {result.get('page')}")
        print(result["text"][:300])
    # 5. Build context from retrieved chunks
    context = ""

    for i, result in enumerate(results, start=1):
        context += f"\n--- Source {i} ---\n"
        context += f"Page: {result.get('page')}\n"
        context += f"Source: {result.get('source')}\n"
        context += result["text"]
        context += "\n"

    # 6. Send question + context to LLM
    answer = generate_answer(
        question,
        context
    )

    return answer