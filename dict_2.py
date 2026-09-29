student = {"name": "Godwin", "course": "AI Engineering", "score": 85}
for key in student:
    print(key)

for key, value in student.items():
    print(key, value)

if "score" in student:
    print("score is a key in student")
else:
    print("score is not a key in student")

for value in student.values():
    print(value)