

n = input()

items = set(map(int, input().split()))

for _ in range(int(input())):
    cmd = input().split()
    try:
        if len(cmd) > 1: cmd, val = cmd[0], cmd[-1]
        else: cmd, val = cmd[0], None
        if cmd == 'pop': exec(f'items.pop()') 
        else: exec(f'items.{cmd}({int(val)})')   
    except Exception:
        continue
print(*items)
    

# # # print(items)
# # items = [1,2,3,4]
# # # cmd = 'pop'.split()

# # # if len(cmd) > 1: cmd, val = cmd[0], int(cmd[-1])
# # # else: cmd = cmd[0]

# # # print(cmd)
# # # # exec(f'items.{cmd}()')
# # cmd = 'remove 9'.split()[-1]
# # print(cmd)
# # exec(f'items.remove(9)')

# print(items)


# li = [ int(x) for x in '1 2 3 4 5 6 7 8 9'.split()]
# li.pop()
# li.remove(9)
# print(li)