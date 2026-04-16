# Day 9C: JSON Save

import json

student = {"name": "Shreyansh", "marks": 90}

with open("student.json", "w") as file:
    json.dump(student, file)

print("Data saved")