
"""
QueueSense: Synthetic Customer Support Data Generator
All records are simulated for portfolio and learning purposes.
"""

import random
from pathlib import Path
from datetime import datetime, timedelta

import pandas as pd

SEED = 42
NUM_TICKETS = 5000
random.seed(SEED)

OUTPUT_DIR = Path("data")
OUTPUT_DIR.mkdir(exist_ok=True)

categories = {
    "Login & Access": 0.25,
    "Payment": 0.20,
    "Technical Error": 0.25,
    "Account Update": 0.15,
    "Other": 0.15,
}

priorities = ["Low", "Medium", "High", "Critical"]
priority_weights = [0.30, 0.40, 0.23, 0.07]

agents = [f"Agent_{i:02d}" for i in range(1, 16)]

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)
total_hours = int((end_date - start_date).total_seconds() // 3600)

rows = []

for ticket_num in range(1, NUM_TICKETS + 1):
    created_at = start_date + timedelta(
        hours=random.randint(0, total_hours)
    )

    category = random.choices(
        list(categories.keys()),
        weights=list(categories.values()),
        k=1,
    )[0]

    priority = random.choices(
        priorities,
        weights=priority_weights,
        k=1,
    )[0]

    # Simulated service times: higher-priority tickets
    # generally receive faster attention.
    base_hours = {
        "Low": 30,
        "Medium": 18,
        "High": 9,
        "Critical": 4,
    }[priority]

    category_factor = {
        "Login & Access": 0.8,
        "Payment": 1.4,
        "Technical Error": 1.6,
        "Account Update": 0.7,
        "Other": 1.0,
    }[category]

    resolution_hours = round(
        random.expovariate(1 / (base_hours * category_factor)),
        2,
    )

    
    
# Simulate whether a ticket remains open at the reporting date.
# Open tickets are deliberately included for backlog analysis.
    report_date = datetime(2026, 1, 1)

    open_probability = {
        "Low": 0.15,
        "Medium": 0.12,
        "High": 0.10,
        "Critical": 0.08,
    }

    is_open = (
        created_at + timedelta(hours=resolution_hours) > report_date
        or random.random() < open_probability[priority]
    )

    agent = random.choice(agents)

    sla_hours = {
        "Low": 72,
        "Medium": 24,
        "High": 8,
        "Critical": 4,
    }[priority]

    resolved_at = (
        None
        if is_open
        else created_at + timedelta(hours=resolution_hours)
    )

    rows.append({
        "ticket_id": f"QS-{ticket_num:05d}",
        "created_at": created_at,
        "category": category,
        "priority": priority,
        "assigned_agent": agent,
        "status": "Open" if is_open else "Resolved",
        "resolution_hours": (
            None if is_open else resolution_hours
        ),
        "sla_hours": sla_hours,
        "resolved_at": resolved_at,
    })

df = pd.DataFrame(rows)

df.to_csv(OUTPUT_DIR / "support_tickets.csv", index=False)

print("QueueSense dataset created successfully!")
print(f"Total tickets: {len(df):,}")
print(f"Open tickets: {(df['status'] == 'Open').sum():,}")
print(f"Resolved tickets: {(df['status'] == 'Resolved').sum():,}")
print(f"Saved to: {OUTPUT_DIR / 'support_tickets.csv'}")
