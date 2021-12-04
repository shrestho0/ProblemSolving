




students_by_time_one = []
students_by_time_two = []

for i in range(1, 10+1):
    if i == 1: suffix = 'st'
    elif i == 2: suffix = 'nd'
    elif i == 3: suffix = 'rd'
    else: suffix = 'th'
    if i <= 5:
        students_by_time_one.append([i, int(input(f"{i}{suffix} Student Semester: "))])
    else:
        students_by_time_two.append([i, int(input(f"{i}{suffix} Student Semester: "))])

students_by_time_one.sort(reverse=True)
students_by_time_one = sorted(students_by_time_one, key=lambda x: x[1])[::-1]

students_by_time_two.sort(reverse=True)
students_by_time_two = sorted(students_by_time_two, key=lambda x: x[1])[::-1]


string = '\n'

for i, sem in students_by_time_one:
    if i == 1: suffix = 'st'
    elif i == 2: suffix = 'nd'
    elif i == 3: suffix = 'rd'
    else: suffix = 'th'
    string += f"{i}{suffix} Student\n"
else: string += "Cafeteria Break\n\n"

for i, sem in students_by_time_two:
    if i == 1: suffix = 'st'
    elif i == 2: suffix = 'nd'
    elif i == 3: suffix = 'rd'
    else: suffix = 'th'
    string += f"{i}{suffix} Student\n"
else: string += "Cafeteria Closed\n"

print(string)

4
5
3
4
8
2
9
9
7
1
1