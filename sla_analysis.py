import sqlite3

connection = sqlite3.connect("data/queuesense.db")

query = """
SELECT
    priority,
    COUNT(*) AS total_resolved,
    SUM(CASE
        WHEN resolution_hours <= sla_hours THEN 1
        ELSE 0
    END) AS within_sla
FROM support_tickets
WHERE status = 'Resolved'
GROUP BY priority
ORDER BY
    CASE priority
        WHEN 'Critical' THEN 1
        WHEN 'High' THEN 2
        WHEN 'Medium' THEN 3
        WHEN 'Low' THEN 4
    END;
"""

results = connection.execute(query)

print("QUEUESENSE — SLA ANALYSIS")
print("-" * 45)

for priority, total, within_sla in results:
    percentage = within_sla / total * 100
    print(
        f"{priority}: {within_sla}/{total} within SLA "
        f"({percentage:.1f}%)"
    )

connection.close()
