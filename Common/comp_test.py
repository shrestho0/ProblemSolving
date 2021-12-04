# # listo = sorted(list(map(int, input().split())))
# # print(sum(listo[:-1]), sum(listo[1:]))




# # n = input()
# # listo = map(int, input().split())

# # x = [3, 2, 1, 3]
# # print(x.count(max(x)))


# # Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock. 
# # - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# # s = input()
# s = '12:40:22AM'
# BELA = s[-2:]
# s = s[:-2]
# HOUR = int(s.split(':')[0])
# # MIN = int(s.split(':')[1])
# # SEC = int(s.split(':')[2])


# if BELA.lower() == 'pm':
#     if HOUR == 12:
#         print(f'{HOUR}{s[2:]}')
#     else:
#         HOUR += 12
#         if HOUR < 10:
#             HOUR = '0'+str(HOUR)
#             print(f'{HOUR}{s[2:]}')
#         else:
#             print(f'{HOUR}{s[2:]}')
# else:
#     if HOUR == 12:
#         print(f'0{HOUR-12}{s[2:]}')
#     else:
#         HOUR += 0
#         if HOUR < 10:
#             HOUR = '0'+str(HOUR)
#             print(f'{HOUR}{s[2:]}')
#         else:
#             print(f'{HOUR}{s[2:]}')


# # else:
# #     if HOUR == 12:
# #         print(f'{HOUR-12}:{MIN}:{SEC}')
# #     else:
# #         print()

# # print(HOUR, MIN, SEC, BELA)





# 3 1
# 1 1 1 1 1 1





# for _ in range(1,int(input().split()[-1])+1):
#     bulbs = tuple(int(x) for x in input().split())


# print(_)
bulbs = [1, 1,1]

# def minimal_cost(bulbs):
#     costs = {}
#     if len(bulbs) > 2:
#         for i in range(1,len(bulbs)-1):
#             now = bulbs.copy()
#             now[i-1] = 0 if now[i-1] == 1 else 1
#             now[i] = 0 if now[i] == 1 else 1
#             now[i+1] = 0 if now[i] == 1 else 0
#             key = sum(now)
#             costs[key] = i

    
#     key = min(costs.keys())

#     return costs.get(key)

# print(minimal_cost(bulbs))

# def turnOffTheLights(k, c):
#         costs = {}
#         if len(bulbs) > 2:
#             for i in range(1,len(bulbs)-1):
#                 now = bulbs.copy()
#                 now[i-1] = 0 if now[i-1] == 1 else 1
#                 now[i] = 0 if now[i] == 1 else 1
#                 now[i+1] = 0 if now[i] == 1 else 0
#                 key = sum(now)
#                 costs[key] = i

        
#         key = min(costs.keys())

#         return costs.get(key)




