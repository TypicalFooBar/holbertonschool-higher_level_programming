#!/usr/bin/python3
""" Module doc """


import json

def load_from_json_file(filename):
    """ Function doc"""

    with open(filename, 'r') as file:
        jsonObject = json.load(file)
        return jsonObject
