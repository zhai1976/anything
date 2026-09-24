import json
import sys

CONFIG_FILE = "algorithm-target.json"

with open(CONFIG_FILE, "r") as f:
    config = json.load(f)

# Validate root object
if "algorithms" not in config:
    raise Exception("Missing root field: algorithms")

algorithms = config["algorithms"]

if not isinstance(algorithms, dict):
    raise Exception("'algorithms' must be a JSON object")

if len(algorithms) == 0:
    raise Exception("No algorithms defined")

# Validate each algorithm
for algorithm_name, algorithm in algorithms.items():

    print(f"Validating: {algorithm_name}")

    # Algorithm name cannot be empty
    if algorithm_name.strip() == "":
        raise Exception("Algorithm name cannot be empty")

    # Required fields
    required_fields = [
        "codePath",
        "mainFile",
        "targets"
    ]

    for field in required_fields:
        if field not in algorithm:
            raise Exception(
                f"Algorithm '{algorithm_name}' is missing required field '{field}'"
            )

    # codePath validation
    if str(algorithm["codePath"]).strip() == "":
        raise Exception(
            f"Algorithm '{algorithm_name}' has empty codePath"
        )

    # mainFile validation
    if str(algorithm["mainFile"]).strip() == "":
        raise Exception(
            f"Algorithm '{algorithm_name}' has empty mainFile"
        )

    if not str(algorithm["mainFile"]).endswith(".py"):
        raise Exception(
            f"Algorithm '{algorithm_name}' mainFile must end with .py"
        )

    # targets validation
    targets = algorithm["targets"]

    if not isinstance(targets, list):
        raise Exception(
            f"Algorithm '{algorithm_name}' targets must be an array"
        )

    if len(targets) == 0:
        raise Exception(
            f"Algorithm '{algorithm_name}' targets cannot be empty"
        )

    for target in targets:
        if str(target).strip() == "":
            raise Exception(
                f"Algorithm '{algorithm_name}' contains an empty target"
            )

print("Validation passed")
