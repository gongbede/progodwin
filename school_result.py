students = ["Godwin", "John", "Peter", "David", "Michael"]
scores = [85, 45, 72, 38, 90]

for number in range(len(students)):
    if scores[number] >= 50:
        print(students[number], scores[number])