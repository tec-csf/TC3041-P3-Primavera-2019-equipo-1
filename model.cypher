=====Hector Mauricio Gonzalez Coello=====
================A01328258================

docker run --publish=7474:7474 --publish=7687:7687 --volume=$HOME/Documents/neo4j/data:/data  --volume=$HOME/Documents/neo4j-import:/var/lib/neo4j/import --env=NEO4J_AUTH=none neo4j

LOAD CSV WITH HEADERS FROM 'file:///sx-stackoverflow.csv' AS row
WITH toInteger(row.nodeA) AS _nodeA, toInteger(row.nodeB) AS _userB, toInteger(row.relationship) AS _relationship
MERGE (userA {userId: _userA})
MERGE (userB {userId: _userB})
MERGE (userA)-[:AnsweredTo {timestamp:_relationship}]->(userB)