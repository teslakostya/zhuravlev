import json

INPUT_FILENAME = "input.json"


def task() -> float:
    with open(INPUT_FILENAME, encoding="utf-8") as f:
        data = json.load(f)

    total = 0.0
    for item in data:
        total += item["score"] * item["weight"]

    return round(total, 3)


if __name__ == "__main__":
    result = task()
    print(result)
