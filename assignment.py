import json
import math
import os
import csv
import random
from datetime import datetime, timedelta


# Basic distance helper
def get_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


#  delay 
def simulate_delivery_delay():
    return random.randint(0, 30)


# Console visualization 
def visualize_route(agent_loc, warehouse_loc, destination, agent_id, pkg_no):
    print("\n" + "=" * 60)
    print(f"Route - Agent {agent_id} | Package {pkg_no}")
    print("=" * 60)

    d1 = get_distance(agent_loc, warehouse_loc)
    d2 = get_distance(warehouse_loc, destination)

    print(f"\nAgent @ {agent_loc}")
    print("   |")
    print(f"   | {d1:.2f}")
    print("   v")
    print(f"Warehouse @ {warehouse_loc}")
    print("   |")
    print(f"   | {d2:.2f}")
    print("   v")
    print(f"Destination @ {destination}")

    print(f"\nTotal distance: {(d1 + d2):.2f}")
    print("=" * 60)


#  new agent while system is running
def add_dynamic_agent(agents, agent_id, location):
    agents[agent_id] = location
    print(f"[INFO] Agent {agent_id} joined at {location}")
    return agents


# Export summary + logs
def export_to_csv(report, output_file, delivery_logs):
    summary_csv = output_file.replace(".json", ".csv")

    with open(summary_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Agent ID",
            "Packages Delivered",
            "Total Distance",
            "Efficiency",
            "Best Agent",
            "Avg Delay (min)"
        ])

        best_agent = report.get("best_agent")

        for agent_id, data in report.items():
            if agent_id in ("best_agent", "dynamic_agents_added"):
                continue

            writer.writerow([
                agent_id,
                data["packages_delivered"],
                data["total_distance"],
                data["efficiency"],
                "Yes" if agent_id == best_agent else "No",
                data.get("avg_delay", 0)
            ])

    print(f"✓ CSV created: {summary_csv}")

    logs_csv = output_file.replace(".json", "_delivery_logs.csv")
    with open(logs_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Package No",
            "Agent",
            "Warehouse",
            "Distance",
            "Delay (min)",
            "Timestamp"
        ])
        writer.writerows(delivery_logs)

    print(f"✓ Logs CSV created: {logs_csv}")


def process_file(input_file, output_file, show_routes=False, dynamic_agents=False):
    with open(input_file) as f:
        data = json.load(f)

    warehouses = data["warehouses"]
    agents = data["agents"].copy()
    packages = data["packages"]

    report = {}
    delivery_logs = []
    agent_delays = {a: [] for a in agents}
    dynamic_added = []

    for agent in agents:
        report[agent] = {
            "packages_delivered": 0,
            "total_distance": 0.0,
            "total_delay": 0
        }

    total_pkgs = len(packages)

    for idx, pkg in enumerate(packages, start=1):

        # Add agents mid-way if enabled
        if dynamic_agents and total_pkgs > 4:
            if idx in (total_pkgs // 4, total_pkgs // 2):
                new_id = f"agent_{len(agents) + 1}"
                new_loc = [random.randint(0, 100), random.randint(0, 100)]
                add_dynamic_agent(agents, new_id, new_loc)

                agents[new_id] = new_loc
                report[new_id] = {
                    "packages_delivered": 0,
                    "total_distance": 0.0,
                    "total_delay": 0
                }
                agent_delays[new_id] = []
                dynamic_added.append(new_id)

        warehouse_id = pkg["warehouse"]
        warehouse_loc = warehouses[warehouse_id]

        # Pick nearest agent
        chosen_agent = None
        min_dist = float("inf")

        for agent_id, agent_loc in agents.items():
            d = get_distance(agent_loc, warehouse_loc)
            if d < min_dist:
                min_dist = d
                chosen_agent = agent_id

        agent_loc = agents[chosen_agent]
        destination = pkg["destination"]

        distance = (
            get_distance(agent_loc, warehouse_loc) +
            get_distance(warehouse_loc, destination)
        )

        delay = simulate_delivery_delay()
        agent_delays[chosen_agent].append(delay)

        if show_routes and idx <= 3:
            visualize_route(agent_loc, warehouse_loc, destination, chosen_agent, idx)

        report[chosen_agent]["packages_delivered"] += 1
        report[chosen_agent]["total_distance"] += distance
        report[chosen_agent]["total_delay"] += delay

        delivery_logs.append([
            idx,
            chosen_agent,
            warehouse_id,
            round(distance, 2),
            delay,
            (datetime.now() + timedelta(minutes=delay)).strftime("%Y-%m-%d %H:%M:%S")
        ])

    # Calculate efficiency
    best_agent = None
    best_eff = float("inf")

    for agent, data in report.items():
        count = data["packages_delivered"]

        if count == 0:
            data["efficiency"] = 0
            data["avg_delay"] = 0
            continue

        data["total_distance"] = round(data["total_distance"], 2)
        data["efficiency"] = round(data["total_distance"] / count, 2)
        data["avg_delay"] = round(data["total_delay"] / count, 2)

        if data["efficiency"] < best_eff:
            best_eff = data["efficiency"]
            best_agent = agent

    report["best_agent"] = best_agent
    if dynamic_added:
        report["dynamic_agents_added"] = dynamic_added

    with open(output_file, "w") as f:
        json.dump(report, f, indent=4)

    print(f"✓ JSON created: {output_file}")
    export_to_csv(report, output_file, delivery_logs)


print("=" * 60)
print("DELIVERY SYSTEM RUN")
print("=" * 60)

for i in range(1, 11):
    input_file = f"test_case_{i}.json"
    output_file = f"test_case_report_{i}.json"

    if os.path.exists(input_file):
        print(f"\nProcessing {input_file}")
        process_file(
            input_file,
            output_file,
            show_routes=(i == 1),
            dynamic_agents=True
        )

        print("\nProcessing completed.")

print("\nAll test cases completed.")
