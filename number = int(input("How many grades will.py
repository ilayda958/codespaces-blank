number = int(input("How many grades will you enter? "))

total = 0

for i in range(number):
    grade = float(input("Enter a grade (1-6): "))
    total = total + grade

average = total / number

print("Average:", round(average, 2))

if average >= 3.0:
    print("Student passed.")
else:
    print("Student failed.")
    