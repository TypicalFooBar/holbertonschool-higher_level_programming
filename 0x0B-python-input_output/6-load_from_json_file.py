import json

def load_from_json_file(filename):
    with open(filename, 'r') as file:
        jsonObject = json.load(file)
        return jsonObject
