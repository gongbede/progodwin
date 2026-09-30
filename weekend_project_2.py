grade_book = {
    "Godwin": {"course": "AI Engineering", "score": 95},
    "Regine": {"course": "Web Dev", "score": 80},
    "Miracle": {"course": "Computer Science", "score": 85},
    "Mohammed": {"course": "Capinter", "score":  90}

}

grade_book["Reuben"] = {"course": "Electrical Engineering", "score": 78}

for name, info in grade_book.items():
    print(name, "-", info["course"], "-", info["score"])

print(grade_book.get("Kayla", "Not Found"))

highest_score = 0
best_score = None

for name, info in grade_book.items():
    if info["score"] > highest_score:
        highest_score = info["score"]
        best_score = name

print(best_score, highest_score)

