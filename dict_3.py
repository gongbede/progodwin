students = {
    "Godwin": {"course": "AI Enginering", "score": 85},
    "Ada": {"course": "Web Dev", "score": 90}

}

print(students.get("Godwin")["course"])
print(students.get("age", "unknown"))
print(students["Ada"]["score"])
for key, value in students.items():
    print(key, "-", value["course"], "-", value["score"])
