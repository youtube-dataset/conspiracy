import json 

def return_conspiracy_theories_titles():
    with open("../data/conspiracy_theories_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return [d["title"] for d in data]

print(return_conspiracy_theories_titles())