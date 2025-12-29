import json
import yaml
import sys
from pathlib import Path

input_file = Path("input-json/api.json")
output_file = Path("generated-yaml/api.yaml")

# Load JSON
with open(input_file, "r") as f:
    data = json.load(f)

# Write YAML
with open(output_file, "w") as f:
    yaml.dump(data, f, sort_keys=False)

print("JSON validated and converted to YAML successfully")
