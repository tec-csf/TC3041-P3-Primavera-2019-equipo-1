from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687")

def get_top_contributors(tx):
    print("Top 10 contributors")
    for record in tx.run("MATCH (g)-[relationship:AnsweredTo]->(n) "
                        "RETURN g.userId, count(relationship) AS responses ORDER BY responses DESC "
                        "LIMIT 10"):
        print(record["g.userId"])

def last_active_users(tx):
    print("Last 10 active users")
    for record in tx.run("MATCH (g)-[relationship:AnsweredTo]->(n) "
                        "RETURN g.userId, relationship.timestamp ORDER BY relationship.timestamp DESC "
                        "LIMIT 10"):
        print(record["g.userId"])

with driver.session() as session:
    session.read_transaction(get_top_contributors)
    session.read_transaction(last_active_users)
