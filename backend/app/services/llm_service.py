import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(question, context):

    prompt = f"""
You are Scholar.AI, an academic research assistant.

Answer the question using ONLY the information
provided in the research paper context.

Do not use outside knowledge.

If the answer cannot be found in the context, say:

"The information is not available in the provided research paper."

Give a clear and concise answer.

Research paper context:

{context}

Question:

{question}
"""

    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=prompt
    )

    return response.text