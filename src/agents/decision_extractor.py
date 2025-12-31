import json
from pathlib import Path
from src.llm.openai_client import call_llm

PROMPT_PATH = Path("src/prompts/decision_extraction.txt")

def extract_decision(text):
    prompt = PROMPT_PATH.read_text() + "\n\nTEXT:\n" + text
    response = call_llm(prompt)
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON from LLM")
