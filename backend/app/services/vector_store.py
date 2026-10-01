import json
import faiss
import numpy as np


def save_embeddings(data, file_path="embeddings.json"):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_embeddings(file_path="embeddings.json"):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

import math


def cosine_similarity(vector1, vector2):
    dot_product = sum(a * b for a, b in zip(vector1, vector2))

    magnitude1 = math.sqrt(sum(a * a for a in vector1))
    magnitude2 = math.sqrt(sum(b * b for b in vector2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0

    return dot_product / (magnitude1 * magnitude2)


def search_similar_chunks(query_embedding, stored_data, top_k=3):
    results = []

    for item in stored_data:
        score = cosine_similarity(
            query_embedding,
            item["embedding"]
        )

        results.append({
            "text": item["text"],
            "score": score
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:top_k]

def build_faiss_index(stored_data):
    vectors = np.array(
        [item["embedding"] for item in stored_data],
        dtype="float32"
    )

    dimension = vectors.shape[1]

    index = faiss.IndexFlatIP(dimension)

    faiss.normalize_L2(vectors)

    index.add(vectors)

    return index

def search_faiss(query_embedding, index, stored_data, top_k=3):
    query_vector = np.array(
        [query_embedding],
        dtype="float32"
    )

    faiss.normalize_L2(query_vector)

    scores, indices = index.search(query_vector, top_k)

    results = []

    for score, idx in zip(scores[0], indices[0]):
        if idx == -1:
            continue

        results.append({
            "chunk_id": stored_data[idx]["chunk_id"],
            "text": stored_data[idx]["text"],
            "score": float(score)
        })

    return results