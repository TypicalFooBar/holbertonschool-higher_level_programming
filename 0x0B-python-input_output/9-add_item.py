#!/usr/bin/python3
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = "add_item.json"
data = []

try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []

for i in range(1, len(sys.argv)):
    data.append(sys.argv[i])

save_to_json_file(data, filename)
