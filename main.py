import json

with open("kaland.json", "r", encoding="utf-8") as f:
    data = json.load(f)

    print(data["bevezeto"])