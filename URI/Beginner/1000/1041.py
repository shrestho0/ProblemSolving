# Accepted in second chance
# Mistake was, Did not read the total plot
get_cords = input().split(' ')

get_x = float(get_cords[0])
get_y = float(get_cords[1])

if get_x == 0 and get_y == 0:
    print("Origem")
elif get_y == 0 and get_x != 0:
    print("Eixo X")
elif get_x == 0 and get_y != 0:
    print("Eixo Y")
elif get_x > 0 and get_y > 0:
    print("Q1")
# Q2
elif get_x < 0 and get_y > 0:
    print("Q2")
# Q3
elif get_x < 0 and get_y < 0:
    print("Q3")
# Q4
elif get_x > 0 and get_y < 0:
    print("Q4")