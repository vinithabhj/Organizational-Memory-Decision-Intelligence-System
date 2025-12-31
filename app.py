import streamlit as st
from src.rag.vector_store import create_vector_store
from src.rag.retriever import retrieve_context
from src.agents.reasoning_agent import answer_question
from src.agents.decision_extractor import extract_decision
from src.graph.graph_builder import store_decision
from src.agents.agent_orchestrator import run_agent_pipeline


texts = []
try:
    raw_text = open("data/raw/sample_meeting.txt").read()

    decision = extract_decision(raw_text)
    store_decision(decision)


    decision_text = f"""
    Decision: {decision['decision']}
    Rationale: {decision['rationale']}
    Alternatives: {decision.get('alternatives')}
    Assumptions: {decision.get('assumptions')}
    """

    texts.append(decision_text)

except:
    texts = ["Decision: Use microservices. Rationale: scalability."]

vector_store = create_vector_store(texts)

st.title("Organizational Memory AI")

query = st.text_input("Ask a question")

if query:
    final_answer = run_agent_pipeline(query, vector_store)
    st.write(final_answer)
