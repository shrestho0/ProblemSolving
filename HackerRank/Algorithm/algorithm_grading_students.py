


# print((73//5 +1)*5 - 73)  
# print((67//5 +1)*5 - 67)
# print((38//5 +1)*5 - 38)
# print()

def gradingStudents(grades):

    for i, grade in enumerate(grades):
        if grade >= 38:
            remainder = (grade//5 +1)*5 - grade
            if remainder <= 2:
                grades[i] += remainder

    return grades
    # Write your code here

if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(*result)