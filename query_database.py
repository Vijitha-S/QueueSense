
import sqlite3

connection = sqlite3.connect("data/queuesense.db")

query = """
SELECT priority, COUNT(*) AS ticket_count
FROM support_tickets
GROUP BY priority
ORDER BY ticket_count DESC;
"""

results = connection.execute(query)

print("QUEUESENSE — SQL PRIORITY REPORT")
print("-" * 35)

for row in results:
    print(f"{row[0]}: {row[1]} tickets")

connection.close()
