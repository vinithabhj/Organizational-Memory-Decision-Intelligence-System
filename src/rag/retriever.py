from src.graph.graph_builder import get_related_decisions

def retrieve_context(query, vector_store):
    # 1. Vector-based retrieval
    docs = vector_store.similarity_search(query, k=3)
    text_context = "\n".join([d.page_content for d in docs])

    # 2. Graph-based retrieval
    graph_results = get_related_decisions(query)
    graph_context = ""

    for g in graph_results:
        graph_context += f"\nDecision: {g['name']}\nRationale: {g['rationale']}\n"

    # 3. Combined context
    combined_context = f"""
    TEXT CONTEXT:
    {text_context}

    GRAPH CONTEXT:
    {graph_context}
    """

    return combined_context
