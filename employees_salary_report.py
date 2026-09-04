employees = ["Godwin", "John","Peter", "David"]
salaries = [120000, 80000,150000,60000]

for number in range(len(employees)):
    if salaries[number] >= 100000:
        print(employees[number], salaries[number], "High salary")

    else:
        print(employees[number], salaries[number])