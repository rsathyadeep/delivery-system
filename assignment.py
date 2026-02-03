import json
import math
import os


def get_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def process_file(input_file, output_file):
    with open(input_file, "r") as f:
        data = json.load(f)

    warehouses = data["warehouses"]
    agents = data["agents"]
    packages = data["packages"]

    report = {}

    # Initialize report for each agent
    for agent in agents:
        report[agent] = {
            "packages_delivered": 0,
            "total_distance": 0.0
        }

    # Process each package
    for pkg in packages:
        warehouse_id = pkg["warehouse"]
        warehouse_location = warehouses[warehouse_id]

        # ASSUMPTION: Find nearest agent to warehouse using Euclidean distance
        # If multiple agents are equidistant, first one in iteration order is selected
        nearest_agent = None
        shortest_distance = float("inf")

        for agent_id, agent_location in agents.items():
            d = get_distance(agent_location, warehouse_location)
            if d < shortest_distance:
                shortest_distance = d
                nearest_agent = agent_id

        # ASSUMPTION: Agent position remains static (doesn't update after delivery)
        agent_location = agents[nearest_agent]
        destination = pkg["destination"]

        # Calculate total travel: agent -> warehouse -> destination
        travel_distance = (
            get_distance(agent_location, warehouse_location) +
            get_distance(warehouse_location, destination)
        )

        report[nearest_agent]["packages_delivered"] += 1
        report[nearest_agent]["total_distance"] += travel_distance

    # Calculate efficiency (lower is better)
    # ASSUMPTION: Efficiency = total_distance / packages_delivered
    best_agent = None
    best_efficiency = float("inf")

    for agent in report:
        count = report[agent]["packages_delivered"]

        if count > 0:
            total = round(report[agent]["total_distance"], 2)
            efficiency = round(total / count, 2)

            report[agent]["total_distance"] = total
            report[agent]["efficiency"] = efficiency

            # ASSUMPTION: In case of tie, first agent with best efficiency wins
            if efficiency < best_efficiency:
                best_efficiency = efficiency
                best_agent = agent
        else:
            # ASSUMPTION: Agents with 0 deliveries get efficiency = 0
            report[agent]["efficiency"] = 0

    report["best_agent"] = best_agent

    with open(output_file, "w") as f:
        json.dump(report, f, indent=4)

    print(f"Generated {output_file}")


# Process all test cases (1-10)
for i in range(1, 11):
    input_name = f"test_case_{i}.json"
    output_name = f"test_case_report_{i}.json"

    if os.path.exists(input_name):
        process_file(input_name, output_name)