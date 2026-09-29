numbers = [12, 45, 7, 89, 23]
biggest = numbers[0]

for number in numbers:
    if number > biggest:
        biggest = number

print(biggest)