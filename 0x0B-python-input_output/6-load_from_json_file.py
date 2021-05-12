#!/usr/bin/python3
import json
""" Module doc """


def load_from_json_file(filename):
    """ Function doc"""

    with open(filename, 'r') as file:
        jsonObject = json.load(file)
        return jsonObject
