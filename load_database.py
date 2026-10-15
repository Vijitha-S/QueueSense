
import sqlite3
from pathlib import Path

import pandas as pd

DATA_FILE = Path("data/support_tickets.csv")
DB_FILE = Path("data/queuesense.db")
SCHEMA_FILE = Path("schema.sql")

# Check that our input files exist.
for file_path in [DATA_FILE, SCHEMA_FILE]:
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

# Load our CSV.
df = pd.read_csv(DATA_FILE)

# Create the SQLite database and table.
with sqlite3.connect(DB_FILE) as connection:
    schema = SCHEMA_FILE.read_text(encoding="utf-8")
    connection.executescript(schema)

    # Load the tickets into SQL.
    df.to_sql(
        "support_tickets",
        connection,
        if_exists="replace",
        index=False,
    )

    # Verify the number of imported records.
    count = connection.execute(
        "SELECT COUNT(*) FROM support_tickets"
    ).fetchone()[0]

print("QueueSense database created successfully!")
print(f"Records imported: {count:,}")
print(f"Database location: {DB_FILE}")
