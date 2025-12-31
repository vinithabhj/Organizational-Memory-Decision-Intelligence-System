from src.graph.neo4j_client import Neo4jClient

def store_decision(decision):
    db = Neo4jClient()
    query = '''
    MERGE (d:Decision {name: $decision})
    SET d.date = $date, d.rationale = $rationale
    '''
    db.run(query, {
        "decision": decision["decision"],
        "date": decision.get("date"),
        "rationale": decision.get("rationale")
    })
    db.close()

def get_related_decisions(decision_name):
    db = Neo4jClient()

    query = """
    MATCH (d:Decision)
    WHERE d.name CONTAINS $name
    RETURN d.name AS name, d.rationale AS rationale
    """

    records = db.run(query, {"name": decision_name})
    db.close()
    return records

