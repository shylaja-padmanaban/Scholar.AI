import math


def cosine_similarity(vector1, vector2):

    dot_product = sum(
        a * b for a, b in zip(vector1, vector2)
    )

    magnitude1 = math.sqrt(
        sum(a * a for a in vector1)
    )

    magnitude2 = math.sqrt(
        sum(b * b for b in vector2)
    )

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0

    return dot_product / (magnitude1 * magnitude2)


def search_similar_chunks(
    query_embedding,
    stored_data,
    top_k=3,
    threshold=0.5
):
    results = []

    for item in stored_data:

        score = cosine_similarity(
            query_embedding,
            item["embedding"]
        )

        if score >= threshold:
            results.append({
                "chunk_id": item.get("chunk_id"),
                "text": item["text"],
                "score": score,
                "page": item.get("page"),
                "source": item.get("source")
            })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:top_k]