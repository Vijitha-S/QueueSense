
-- QueueSense: Customer Support Analytics
-- All records are simulated for learning and portfolio use.

CREATE TABLE IF NOT EXISTS support_tickets (
    ticket_id TEXT PRIMARY KEY,
    created_at TEXT NOT NULL,
    category TEXT NOT NULL,
    priority TEXT NOT NULL,
    assigned_agent TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('Open', 'Resolved')),
    resolution_hours REAL,
    sla_hours INTEGER NOT NULL,
    resolved_at TEXT
);
