

#@ Leaning Part

# from collections import namedtuple

# Point = namedtuple('Point', 'x,y')

# pt1 = Point(1,2)
# pt2 = Point(3,4)

# dot_product = pt1.x * pt2.x + pt1.y * pt2.y
# print(dot_product)



# Car = namedtuple('Car', 'Price Mileage Color Class')
# car = Car(100000, 30, 'Cyan', 'C')
# print(car.Class)

from collections import namedtuple

# TASK
# 5
# ID         MARKS      NAME       CLASS     
# 1          97         Raymond    7         
# 2          50         Steven     4         
# 3          91         Adrian     9         
# 4          72         Stewart    5         
# 5          80         Peter      6   

def typed(string):
    if string.isdigit():
        return int(string)
    return string



n = int(input())
Students = namedtuple("Student", ' '.join(input().split()))
tups_data = {}
total_num = []
for i in range(n):
    total_num.append(Students(*list(map(typed, input().split()))).MARKS)

print(f'{(sum(total_num)/n):.2f}')


# 5
# MARKS      CLASS      NAME       ID        
# 92         2          Calum      1         
# 82         5          Scott      2         
# 94         2          Jason      3         
# 55         8          Glenn      4         
# 82         2          Fergus     5
# OUTPUT: 81.00
