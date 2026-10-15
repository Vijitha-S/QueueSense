
from pathlib import Path
import pandas as pd

# Load our generated dataset
file_path = Path("data/support_tickets.csv")
df = pd.read_csv(file_path)

print("=" * 45)
print("QUEUESENSE — DATA QUALITY REPORT")
print("=" * 45)

# 1. Dataset size
print(f"\nTotal rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")

# 2. Duplicate ticket IDs
print(f"\nDuplicate ticket IDs: {df['ticket_id'].duplicated().sum()}")

# 3. Missing values
print("\nMissing values by column:")
print(df.isnull().sum().to_string())

# 4. Ticket status
print("\nTicket status counts:")
print(df["status"].value_counts().to_string())

# 5. Priority distribution
print("\nPriority distribution:")
print(df["priority"].value_counts().to_string())

# 6. Category distribution
print("\nTicket categories:")
print(df["category"].value_counts().to_string())

# 7. Check invalid resolution times
resolved = df[df["status"] == "Resolved"]
invalid_times = (resolved["resolution_hours"].isna()).sum()
negative_times = (resolved["resolution_hours"].dropna() < 0).sum()

print(f"\nResolved tickets without resolution time: {invalid_times}")
print(f"Negative resolution times: {negative_times}")

print("\nData validation report completed.")
