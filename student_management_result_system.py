def calculate_total(scores):
    total = 0
    for number in range(len(scores)):
        total = total + scores[number]
    return total

def check_result(score):
    if score >= 50:
        return "Passed"

    else:
        return "Failed"

def count_passed(scores):
    count = 0

    for number in range(len(scores)):
        if scores[number] >= 50:
            count = count + 1

        
    return count


def count_failed(scores):
    count = 0 

    for number in range(len(scores)):
        if scores[number] < 50:
            count = count + 1

    return count


students = ["Godwin", "John", "Peter", "David", "Michael"]
scores = [85, 45, 72, 38, 90]

for number in range(len(students)):
        print(students[number], scores[number], check_result(scores[number]))


total_scores = calculate_total(scores)
print("Total Scores:",    total_scores)
print("Total Passed", count_passed(scores))
print("Total Failed", count_failed(scores))