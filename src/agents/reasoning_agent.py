from src.llm.openai_client import call_llm

def answer_question(question, context):
    prompt = f"""Use the context to answer clearly.

Context:
{context}

Question:
{question}
"""
    return call_llm(prompt)
