from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

def add_friend(tx, name, friend_name):
    tx.run("MERGE (a:Person {name: $name}) "
           "MERGE (a)-[:KNOWS]->(friend:Person {name: $friend_name})",
           name=name, friend_name=friend_name)

def print_friends(tx, name):
    for record in tx.run("MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
                         "RETURN friend.name ORDER BY friend.name", name=name):
        print(record["friend.name"])

def get_top_contributors(tx):
    print("Top 10 contributors")
    for record in tx.run("MATCH (g:Node)-[relationship:RESPONDED]->(n:Node) "
                        "RETURN g.userID, count(relationship) AS responses ORDER BY responses DESC "
                        "LIMIT 10"):
        print(record["g.userID"])

def last_active_users(tx):
    print("Last 10 active users")
    for record in tx.run("MATCH (g:Node)-[relationship:RESPONDED]->(n:Node) "
                        "RETURN g.userID, relationship.timestamp ORDER BY relationship.timestamp DESC "
                        "LIMIT 100"):
        print(record["g.userID"])

def path_between_users(u_id1, u_id2):
    print("The shortest path between user {u_id1} and user {u_id2} is "
    for record in tx.run("MATCH (user1:Node { userID:$u_id1 }),(user2:Node { userID:$u_id2 }), "
                        "p = shortestPath((user1)-[*..5]-(user2))"
                        "RETURN length(p)", u_id1=u_id1, u_id2=u_id2):
        print(record["friend.name"])

with driver.session() as session:
    session.write_transaction(add_friend, "Arthur", "Guinevere")
    session.write_transaction(add_friend, "Arthur", "Lancelot")
    session.write_transaction(add_friend, "Arthur", "Merlin")
    session.read_transaction(print_friends, "Arthur")
