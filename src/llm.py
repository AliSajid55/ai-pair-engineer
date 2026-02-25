import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")


def get_client() -> genai.Client:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY in .env")

    return genai.Client(api_key=api_key)


def chat_json(system: str, user: str) -> str:
    client = get_client()
    model = os.getenv("GEMINI_MODEL", "gemini-2.0-flash-lite")

    response = client.models.generate_content(
        model=model,
        contents=user,
        config=types.GenerateContentConfig(
            system_instruction=system,  # type: ignore[call-arg]
            temperature=0.2,  # type: ignore[call-arg]
        ),
    )
    return response.text or ""