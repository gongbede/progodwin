employees = ["Godwin", "John", "Peter", "David", "Michael", "Sarah"]
salaries = [120000, 80000,150000, 60000,95000,200000]

high_salary_count = 0
normal_salary_count = 0

for number in range(len(employees)):
    if salaries[number] >= 100000:
        print(employees[number], salaries[number], "High Salary")
        high_salary_count = high_salary_count + 1

    else:
        print(employees[number], salaries[number], "Normal Salary")
        normal_salary_count = normal_salary_count + 1

print("Total High Salary", high_salary_count)
print("Total Normal Salary", normal_salary_count)
