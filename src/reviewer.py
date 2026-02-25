import json
import re
from .llm import chat_json
from .prompts import PAIR_ENGINEER_SYSTEM, build_user_prompt
from google.genai.errors import ClientError


def _strip_markdown_fences(text: str) -> str:
    """Remove ```json ... ``` wrappers that LLMs often add around JSON."""
    text = text.strip()
    match = re.match(r"^```(?:json)?\s*\n(.*?)```\s*$", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text

def review_code(language: str, code: str, extra_context: str = "") -> dict:
    user_prompt = build_user_prompt(language, code, extra_context)
    try:
        raw = chat_json(PAIR_ENGINEER_SYSTEM, user_prompt)
    except ClientError as e:
        if e.code == 429:
            return {
                "summary": "Rate limit exceeded. Gemini free tier has per-minute limits. Please wait 1-2 minutes and try again.",
                "design_flaws": [],
                "tests": [],
                "refactor": {"goals": [], "patch": ""},
                "_error": "rate_limit",
            }
        return {
            "summary": f"API error: {e.message or str(e)}",
            "design_flaws": [],
            "tests": [],
            "refactor": {"goals": [], "patch": ""},
            "_error": str(e),
        }

    # Strip markdown fences and parse JSON
    raw = _strip_markdown_fences(raw)
    try:
        data = json.loads(raw)
    except Exception as e:
        # Fallback: return raw so UI can show it (don't crash)
        return {
            "summary": "Model did not return valid JSON. Showing raw output.",
            "design_flaws": [],
            "tests": [],
            "refactor": {"goals": [], "patch": raw},
            "_error": str(e),
            "_raw": raw
        }
    return data