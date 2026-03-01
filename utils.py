import json
import os

def save_to_json(filename, data):
    os.makedirs("data", exist_ok=True)

    with open(f"data/{filename}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
