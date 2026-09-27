def find_student(students, name):

    for student in students:
        if student == name:
            return True

    return False

students = ["Godwin", "John", "Peter", "David", "Michael"]
result = find_student(students, "Peter")
print(result)
result = find_student(students, "James")
print(result)