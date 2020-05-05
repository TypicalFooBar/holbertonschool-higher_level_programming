#!/usr/bin/python3
import json


def load_from_json_file(filename):
    jsonString = ""

    with open(filename) as f:
        jsonString = f.read()
    f.close()

    return json.loads(jsonString)
