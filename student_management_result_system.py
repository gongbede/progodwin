students = ["Godwin", "John", "Peter", "David", "Michael"]
scores = [85, 45, 72, 38, 90]

pass_student_count = 0
fail_student_count = 0

total_scores = 0

for number in range(len(students)):
    if scores[number] >= 50:
        print(students[number], scores[number], "Passed")
        pass_student_count = pass_student_count + 1

        total_scores = total_scores + scores[number]


    else:
        print(students[number], scores[number], "Failed")
        fail_student_count = fail_student_count + 1

        total_scores = total_scores + scores[number]



print(pass_student_count, "Total passed")
print(fail_student_count, "Total Failed")
print(total_scores)