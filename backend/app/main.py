from services.pdf_service import extract_text_from_pdf
from services.text_processor import clean_text, split_into_chunks


def main():

    pdf_path = "../../data/papers/research_paper.pdf"

    # Step 1: Extract PDF text
    raw_text = extract_text_from_pdf(pdf_path)

    print("\n========== RAW TEXT ==========\n")
    print(raw_text[:1000])

    # Step 2: Clean text
    cleaned_text = clean_text(raw_text)

    print("\n========== CLEANED TEXT ==========\n")
    print(cleaned_text[:1000])

    # Step 3: Create chunks
    chunks = split_into_chunks(
        cleaned_text,
        chunk_size=1000,
        chunk_overlap=200
    )

    print("\n========== CHUNKING ==========\n")

    print("Total characters:", len(cleaned_text))
    print("Total chunks:", len(chunks))

    for i, chunk in enumerate(chunks[:3], start=1):

        print(f"\n--- Chunk {i} ---")
        print(chunk[:500])


if __name__ == "__main__":
    main()