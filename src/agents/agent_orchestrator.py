from src.rag.retriever import retrieve_context
from src.agents.reasoning_agent import answer_question


def run_agent_pipeline(query, vector_store):
    """
    Main multi-agent controller.
    """
    # 1️⃣ Retriever Agent
    context = retrieve_context(query, vector_store)

    # 2️⃣ Reasoning Agent
    answer = answer_question(query, context)

    # 3️⃣ Verifier Agent
    final_answer = verify_answer(answer, context)

    return final_answer


def verify_answer(answer, context):
    """
    Improved verifier agent:
    - Checks grounding
    - Computes confidence
    - Explains uncertainty
    """

    if not answer or len(answer.strip()) == 0:
        return format_response(
            "I could not generate a reliable answer.",
            confidence=0.0,
            reason="LLM returned an empty response."
        )

    if not context or len(context.strip()) == 0:
        return format_response(
            "I am not confident enough to answer.",
            confidence=0.1,
            reason="No supporting context was retrieved."
        )

    # --- Grounding check ---
    answer_tokens = set(answer.lower().split())
    context_tokens = set(context.lower().split())

    overlap = answer_tokens.intersection(context_tokens)
    grounding_ratio = len(overlap) / max(len(answer_tokens), 1)

    # --- Decision-aware boost ---
    decision_keywords = ["decision", "rationale", "chosen", "selected", "because"]
    decision_signal = any(word in context.lower() for word in decision_keywords)

    # --- Confidence computation ---
    confidence = min(
        1.0,
        grounding_ratio + (0.2 if decision_signal else 0.0)
    )

    if confidence < 0.3:
        return format_response(
            answer,
            confidence=confidence,
            reason="Weak grounding between answer and stored decisions."
        )

    return format_response(
        answer,
        confidence=confidence,
        reason="Answer is grounded in retrieved decision context."
    )


# ⬇️⬇️⬇️ ADD THIS FUNCTION HERE (JUST BELOW verify_answer) ⬇️⬇️⬇️
def format_response(answer, confidence, reason):
    return f"""
🧠 **Answer**
{answer}

📊 **Confidence**
{round(confidence, 2)}

🔍 **Verifier Explanation**
{reason}
"""

