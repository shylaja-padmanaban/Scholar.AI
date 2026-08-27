from services.vector_store import search_similar_chunks


stored_data = [
    {
        "text": "The dataset contains 10,000 plant leaf images.",
        "embedding": [0.9, 0.1, 0.0]
    },
    {
        "text": "The model uses a convolutional neural network.",
        "embedding": [0.1, 0.9, 0.0]
    },
    {
        "text": "The model achieved 94 percent accuracy.",
        "embedding": [0.0, 0.1, 0.9]
    }
]


query_embedding = [0.85, 0.15, 0.0]

results = search_similar_chunks(
    query_embedding,
    stored_data,
    top_k=2
)

for result in results:
    print("\nScore:", result["score"])
    print("Text:", result["text"])