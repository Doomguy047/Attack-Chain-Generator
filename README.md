# Rule-Based Attack Chain Generator (MITRE ATT&CK)
## Overview
This project implements a rule-based attack chain generator that models adversary behavior using MITRE ATT&CK tactics. 
By focusing on explainable logic and prioritization rather than attack execution, the tool helps reason about likely next steps in an attack and supports both red team planning and incident response prioritization.

It is designed for educational and early-stage analysis purpose that emphasizes explainable attack progression.
"This project prioritizes conceptual clarity and explainability over completeness."
## How It Works
- Accepts a known attack tactic as input
- Applies predefined attack progression rules
- Scores possible next techniques using impact and likelihood
- Outputs a ranked list of next attack steps in JSON format

## Technologies Used
- Python
- MITRE ATT&CK (conceptual mapping)

## Example

### Input
```json
{
  "current_tactic": "Credential Access"
}


