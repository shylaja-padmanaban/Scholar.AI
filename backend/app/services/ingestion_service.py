from services.pdf_service import extract_text_from_pdf
from services.text_processor import create_chunks
from services.embeddings_service import generate_embedding
from services.vector_store import save_embeddings


def ingest_document(pdf_path):

    pages = extract_text_from_pdf(pdf_path)

    all_chunks = []

    for page_data in pages:

        page_number = page_data["page"]
        text = page_data["text"]

        chunks = create_chunks(text)

        for chunk in chunks:

            all_chunks.append({
                "text": chunk,
                "page": page_number,
                "source": pdf_path
            })

    for item in all_chunks:

        item["embedding"] = generate_embedding(item["text"])

    save_embeddings(all_chunks)

    return all_chunks