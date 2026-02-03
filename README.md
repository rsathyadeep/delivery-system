Package Delivery Assignment System
Overview

This project implements a basic package delivery assignment system using Python.
The system assigns packages to the nearest delivery agents based on warehouse locations and calculates delivery performance metrics such as distance, efficiency, and delays.

This project was developed as part of a Python developer assignment to demonstrate problem-solving skills, logical thinking, and clean code structure.

Features
Core Features

Assigns each package to the nearest available delivery agent

Calculates total distance traveled by each agent

Computes delivery efficiency for each agent

Identifies the best-performing agent

Generates structured JSON reports

Additional Features
1. Random Delivery Delays

Simulates real-world delivery delays between 0 and 30 minutes

Tracks average delay per agent

Delay information is included in both JSON and CSV reports

2. ASCII Route Visualization

Displays delivery routes directly in the terminal

Shows the path: agent → warehouse → destination

Displays distance for each segment and total distance

Enabled only for the first 3 packages of the first test case to avoid clutter

Example:

============================================================
Route Visualization - Agent agent_1 | Package #1
============================================================

Agent Location: [10, 20]
    |
    | (25.30 units)
    ▼
Warehouse: [30, 35]
    |
    | (42.72 units)
    ▼
Destination: [60, 65]

Total Distance: 68.02 units
============================================================

3. Dynamic Agent Joining

Supports agents joining during package processing

New agents are added at 25% and 50% progress points

Newly added agents are immediately considered for delivery

Dynamically added agents are recorded in the final report

4. Export to CSV

Generates CSV reports in addition to JSON

Summary CSV shows agent performance

Detailed delivery logs CSV contains individual delivery details

Useful for viewing results in spreadsheet tools

Files Generated

For each test case, the following files are generated:

test_case_report_X.json – main delivery report

test_case_report_X.csv – agent performance summary

test_case_report_X_delivery_logs.csv – detailed delivery logs

Assumptions

Agents are selected based on the shortest distance to the warehouse

If two agents are equally close, the first one encountered is selected

Agent positions remain static and are not updated after deliveries

Distance is calculated using Euclidean (straight-line) distance

Efficiency is calculated as:

efficiency = total_distance / packages_delivered


Agents with zero deliveries are still included in the report

All distance and efficiency values are rounded to two decimal places

Packages are processed sequentially in input order

Delivery delays are random and do not affect agent selection

Dynamic agents receive random coordinates between 0 and 100

How to Run
Run with All Features Enabled
python delivery_system_with_all_bonus.py


This will:

Process all test cases (1–10)

Enable random delays, dynamic agents, visualization, and CSV export

Generate JSON and CSV reports

Run Basic Version (Core Features Only)
python delivery_system.py

Requirements

Python 3.6 or above

Uses only Python standard libraries:

json

math

os

csv

random

datetime

Sample JSON Output
{
    "agent_1": {
        "packages_delivered": 5,
        "total_distance": 245.67,
        "efficiency": 49.13,
        "avg_delay": 15.0
    },
    "best_agent": "agent_1",
    "dynamic_agents_added": ["agent_4", "agent_5"]
}

Example Terminal Output
============================================================
DELIVERY SYSTEM - ALL FEATURES ENABLED
============================================================

Processing: test_case_1.json

[INFO] Agent agent_4 joined at location [45, 78]
[INFO] Agent agent_5 joined at location [23, 91]

✓ JSON generated
✓ CSV generated
✓ Delivery logs generated

Summary

Core delivery logic implemented successfully

Additional features added to simulate real-world behavior

Code is modular, readable, and easy to extend

Outputs available in both JSON and CSV formats

Author: Sathya Deep Reddy
Date: 3rd February 2026