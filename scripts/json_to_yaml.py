import json
import yaml
from pathlib import Path

# Define paths
input_file = Path("input-json/api.json")
output_dir = Path("generated-yaml")
output_file = output_dir / "api.yaml"

# Create output directory if it does not exist
output_dir.mkdir(parents=True, exist_ok=True)

# Load JSON
with open(input_file, "r") as f:
    data = json.load(f)

# Write YAML
with open(output_file, "w") as f:
    yaml.dump(data, f, sort_keys=False)

print(f"JSON validated and converted to YAML: {output_file}")
