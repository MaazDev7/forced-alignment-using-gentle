import json

with open("aligned.json", "r") as f:
    data = json.load(f)

for word in data["words"]:
    if word.get("case") == "success":  # Only keep aligned words
        text = word["word"]
        start = word["start"]
        end = word["end"]
        print(f"{text}: {start:.2f} - {end:.2f} sec")
