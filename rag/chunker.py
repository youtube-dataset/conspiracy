import json 

def read_json():
    # Since they are in the same folder, just use the filename directly
    with open("../data/conspiracy_theories_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return data

print(read_json())