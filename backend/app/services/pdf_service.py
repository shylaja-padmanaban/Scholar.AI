from pathlib import Path
from pypdf import PdfReader


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from every page of a PDF.

    Args:
        file_path: Path to the PDF file.

    Returns:
        All extracted text combined into one string.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("The provided file is not a PDF.")

    reader = PdfReader(str(path))

    pages_text = []

    for page_number, page in enumerate(reader.pages, start=1):

        text = page.extract_text()

        if text:
            pages_text.append(
                f"\n--- Page {page_number} ---\n{text}"
            )

    if not pages_text:
        raise ValueError(
            "No text could be extracted from this PDF. "
            "The PDF may be scanned or image-based."
        )

    return "\n".join(pages_text)