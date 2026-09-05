def calculate_total(scores):
    total = 0
    for number in range(len(scores)):
        total = total + scores[number]
    return total

students = ["Godwin", "John", "Peter", "David", "Michael"]
scores = [85, 45, 72, 38, 90]

pass_student_count = 0
fail_student_count = 0


for number in range(len(students)):
    if scores[number] >= 50:
        print(students[number], scores[number], "Passed")
        pass_student_count = pass_student_count + 1



    else:
        print(students[number], scores[number], "Failed")
        fail_student_count = fail_student_count + 1




print(pass_student_count, "Total passed")
print(fail_student_count, "Total Failed")



total_scores = calculate_total(scores)
print("Total Scores:",    total_scores)