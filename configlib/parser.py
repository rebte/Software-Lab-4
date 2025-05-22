import json
import yaml

def parse_config(path):
    if path.endswith(".json"):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    elif path.endswith(".yaml") or path.endswith(".yml"):
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    else:
        raise ValueError("Unsupported file format. Use .json or .yaml")
