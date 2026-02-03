Handling Scenarios

Some parts of the problem statement did not explicitly define how certain edge cases or ambiguous scenarios should be handled (such as tie-breaking, routing order, or agent behavior after delivery).

As instructed, in such situations I made reasonable engineering decisions based on simplicity, efficiency, and real-world logic, without stopping for clarification. All such decisions are documented below and implemented consistently in the code.

Documented Assumptions

Agent Selection:
If multiple agents are at the same minimum distance from a warehouse, the first agent encountered during iteration is selected.

Agent Movement Model:
Agent locations are considered static and are not updated after completing a delivery.

Distance Calculation:
All distances are calculated using Euclidean (straight-line) distance between coordinates.

Processing Order:
Packages are processed sequentially in the order they appear in the input file.

Efficiency Metric:
Delivery efficiency is calculated as:

efficiency = total_distance / packages_delivered


Lower values indicate better performance.

Best Agent Tie-Breaking:
If multiple agents have the same efficiency score, the first agent encountered is selected as the best agent.

Zero Delivery Agents:
Agents who do not deliver any packages are still included in the report with efficiency set to 0.

Delivery Delays:
Delivery delays are randomly generated (0–30 minutes) and do not affect routing or agent selection.

Dynamic Agent Behavior:
Agents added dynamically during processing are immediately eligible to receive package assignments.

These assumptions were chosen to keep the system deterministic, easy to understand, and efficient, while meeting the requirements of the assignment.

Add simple comments like these in your code.
This proves you didn’t just write assumptions in README — you applied them.

Example 1: Agent Selection Logic
# Select the nearest agent to the warehouse
# If multiple agents are equally close, the first one encountered is selected

Example 2: Static Agent Position
# Agent locations are treated as static
# Agent position is not updated after delivery

Example 3: Efficiency Calculation
# Efficiency is calculated as total_distance / packages_delivered
# Lower value indicates better efficiency

Example 4: Tie-breaking Best Agent
# In case of equal efficiency, the first agent encountered is selected

Example 5: Dynamic Agent Addition
# Dynamically added agents are immediately available for assignment
