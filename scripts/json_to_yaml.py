import json
import yaml
from pathlib import Path

input_dir = Path("input-json")
output_dir = Path("generated-yaml")

# Create output directory if it does not exist
output_dir.mkdir(parents=True, exist_ok=True)

# Loop through all JSON files
for json_file in input_dir.glob("*.json"):
    with open(json_file, "r") as f:
        data = json.load(f)

    yaml_file = output_dir / f"{json_file.stem}.yaml"

    with open(yaml_file, "w") as f:
        yaml.dump(data, f, sort_keys=False)

    print(f"Converted {json_file} -> {yaml_file}")
