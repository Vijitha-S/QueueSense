# QueueSense — Customer Support Analytics Dashboard

## Project Overview
QueueSense is a customer support analytics project that analyzes support tickets to understand ticket volume, resolution time, and Service Level Agreement (SLA) performance.

This project uses a simulated dataset of 5,000 support tickets.

## Objectives
- Monitor total, open, and resolved tickets.
- Analyze average ticket resolution time.
- Compare SLA compliance across priority levels.
- Identify categories that take longer to resolve.
- Present key findings through an interactive Power BI dashboard.

## Tools and Technologies
- Python
- Pandas
- SQL and SQLite
- Power BI
- CSV

## Project Structure
- `data/` — Support ticket dataset and SQLite database
- `reports/` — Generated analysis reports
- `powerbi/` — Power BI dashboard
- Python scripts — Data generation, analysis, database operations, and report export
- SQL scripts — Database schema and queries

## Key Metrics
- Total tickets: 5,000
- Resolved tickets: 4,421
- Open tickets: 579
- Average resolution time for resolved tickets: 20.39 hours

## Key Findings
- Technical Error tickets have the longest average resolution time at 27.74 hours.
- Payment tickets take an average of 25.43 hours to resolve.
- Low-priority tickets have the highest SLA compliance at 88.3%.
- High-priority tickets have the lowest SLA compliance at 56.7%.

## Dashboard
The Power BI dashboard presents ticket volume by priority, SLA performance, resolution time by category, and ticket resolution status.

## Dataset Note
The dataset is simulated for learning and portfolio demonstration. It does not contain real customer support records.

## Future Improvements
- Add more detailed trend analysis.
- Improve SLA monitoring and escalation insights.
- Explore automated reporting.
