employees = ["Godwin", "John","Peter", "David"]
salaries = [120000, 80000,150000,60000]
high_salary_count = 0

for number in range(len(employees)):
    if salaries[number] >= 100000:
        print(employees[number], salaries[number], "High salary")
        high_salary_count = high_salary_count + 1

    else:
        print(employees[number], salaries[number])
print("Total High Salary", high_salary_count)
