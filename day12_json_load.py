# Day 9D: JSON Load

import json

with open("student.json", "r") as file:
    data = json.load(file)

print("Loaded data:", data)