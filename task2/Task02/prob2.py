student = []
names = []
grades = []
num = int(input())

for x in range(num):
    name = input()
    degree = float(input())
    student.append([name, degree])
    grades.append(degree)
    names.append(name)

first_lowest = min(grades)
second_lowest = float('inf')

for grade in grades:
    if grade != first_lowest and grade < second_lowest:
        second_lowest = grade

lowest_names = []
for name, grade in student:
    if grade == second_lowest:
        lowest_names.append(name)

lowest_names.sort()

for name in lowest_names:
    print(name)

