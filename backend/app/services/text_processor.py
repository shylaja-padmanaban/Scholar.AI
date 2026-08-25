import re


def clean_text(text: str) -> str:
    """
    Clean extracted PDF text.
    """

    # Replace multiple spaces/tabs with one space
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Remove leading/trailing whitespace from lines
    lines = [line.strip() for line in text.splitlines()]

    # Remove empty lines at the beginning/end
    text = "\n".join(lines).strip()

    return text


def split_into_chunks(
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> list[str]:
    """
    Split text into overlapping chunks.
    """

    if chunk_overlap >= chunk_size:
        raise ValueError(
            "chunk_overlap must be smaller than chunk_size"
        )

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - chunk_overlap

    return chunks