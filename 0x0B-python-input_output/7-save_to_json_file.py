#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    jsonString = json.dumps(my_obj)

    with open(filename, "w") as f:
        f.write(jsonString)

    f.close()
