
import sqlite3
from pathlib import Path
import pandas as pd

Path("reports").mkdir(exist_ok=True)

connection = sqlite3.connect("data/queuesense.db")

query = """
SELECT
    category,
    priority,
    status,
    COUNT(*) AS ticket_count,
    AVG(resolution_hours) AS avg_resolution_hours,
    SUM(
        CASE
            WHEN status = 'Resolved'
                 AND resolution_hours <= sla_hours
            THEN 1
            ELSE 0
        END
    ) AS within_sla_count
FROM support_tickets
GROUP BY category, priority, status
ORDER BY category, priority, status;
"""

df = pd.read_sql_query(query, connection)
df.to_csv("reports/dashboard_summary.csv", index=False)

connection.close()

print("Dashboard data exported successfully!")
print(f"Summary rows: {len(df)}")
print("Saved to: reports/dashboard_summary.csv")
