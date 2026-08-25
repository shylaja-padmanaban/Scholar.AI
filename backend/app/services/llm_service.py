import os

from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file")

client = genai.Client(api_key=api_key)


SYSTEM_INSTRUCTION = """
You are ScholarAI, an academic research assistant.

Your role is to help students understand academic,
technical, and research-related topics.

Follow these rules:
- Explain concepts clearly and accurately.
- Use simple language when appropriate.
- Organize complex answers using headings or bullet points.
- Do not intentionally invent facts.
- If you are uncertain, clearly say so.
- Do not claim that you accessed a source unless the application
  actually provides that source.
"""


class PaperAnalysis(BaseModel):
    title: str
    research_problem: str
    methodology: str
    dataset: str
    results: str
    limitations: str


def generate_response(user_prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        config={
            "system_instruction": SYSTEM_INSTRUCTION
        },
        contents=user_prompt
    )

    return response.text


def analyze_paper(text: str) -> PaperAnalysis:

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"""
Analyze the following research paper text.

Extract the following information:

- title
- research problem
- methodology
- dataset
- results
- limitations

Research paper text:

{text}
""",
        config={
            "response_mime_type": "application/json",
            "response_schema": PaperAnalysis,
        },
    )

    return PaperAnalysis.model_validate_json(response.text)