# Simple rule-based attack chain generator
# Built to understand attack progression using MITRE ATT&CK concepts

import json
import sys

def score(impact, likelihood):
    """
    Calculate a weighted score for prioritization.
    """
    return round((impact * 0.6) + (likelihood * 0.4), 2)

# Load attack progression rules
with open("mitre_rules.json") as f:
    rules = json.load(f)

# Get current tactic from CLI or input file
if len(sys.argv) > 1:
    current_tactic = sys.argv[1]
else:
    with open("input.json") as f:
        user_input = json.load(f)
        current_tactic = user_input["current_tactic"]

# Fetch possible next steps
results = rules.get(current_tactic, [])

# Score each suggestion
for r in results:
    r["score"] = score(r["impact"], r["likelihood"])

# Rank by score
results = sorted(results, key=lambda x: x["score"], reverse=True)

# Write output
with open("output.json", "w") as f:
    json.dump(results, f, indent=2)

print("Attack chain suggestions generated successfully.")
