
 

from collections import deque

# listo = [1,2,3,4,52,23,13,4]
# listo = deque(listo)
# #append
# listo.append('append')
# print(listo)
# #appendleft
# listo.appendleft('append left')
# print(listo)

# #clear
# listo.clear()
# #count(x)
# print(listo.count('x'))

# #extend
# listo.extend([10])
# print(listo)
# #extendleft
# listo.extend([100])
# print(listo)

# #pop
# listo.pop()
# print(listo)

# #remove
# listo.remove(10)
# print(listo)


# listo.extend([8,5,12,6,7])

# listo.reverse()
# print(listo)

# listo.rotate(2)
# print(listo)




# d = deque([1,2,3])
# commands = []
# for i in range(int(input())):
#     command = input().split()
#     commands+=command




# print(*d)

# print(commands)


# x = "print([1,2,3,4,5 ,5,4])"
# # x = eval(x)

# exec(x)
# command = exec(command)

listo = deque([])
for i in range(int(input())):
    get_cmd = input().strip().split()

    if len(get_cmd) > 1:
        get_cmd = f"listo.{get_cmd[0]}({get_cmd[-1]})"
    else:
        get_cmd = f"listo.{get_cmd[0]}()"

    print(get_cmd)
    exec(get_cmd)


print(*listo)





