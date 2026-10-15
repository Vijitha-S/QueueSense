
from pathlib import Path
import pandas as pd

df = pd.read_csv("data/support_tickets.csv")

# Convert date columns
df["created_at"] = pd.to_datetime(df["created_at"])
df["resolved_at"] = pd.to_datetime(df["resolved_at"])

total = len(df)
open_tickets = (df["status"] == "Open").sum()
resolved = df[df["status"] == "Resolved"]

print("=" * 45)
print("QUEUESENSE — BUSINESS KPI REPORT")
print("=" * 45)

print(f"\nTotal tickets: {total:,}")
print(f"Open tickets: {open_tickets:,}")
print(f"Resolved tickets: {len(resolved):,}")
print(f"Open ticket rate: {open_tickets / total:.1%}")

print(
    f"\nAverage resolution time: "
    f"{resolved['resolution_hours'].mean():.2f} hours"
)

print("\nTickets by priority:")
print(df.groupby("priority").size().sort_values(ascending=False))

print("\nAverage resolution time by category:")
print(
    resolved.groupby("category")["resolution_hours"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

print("\nTickets by status:")
print(df["status"].value_counts())

# Save a reusable summary for later reporting
Path("reports").mkdir(exist_ok=True)

summary = (
    resolved.groupby("category")["resolution_hours"]
    .agg(["count", "mean", "median"])
    .round(2)
)

summary.to_csv("reports/category_resolution_summary.csv")

print("\nSaved: reports/category_resolution_summary.csv")
