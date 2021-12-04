# def wands(list1, list2):
#     list2.sort()
#     count = 0
#     for x in range(len(list2)-1):
#         if abs(list2[x-1]) - abs(list2[x]) > list1[1]:
#             count += 1
#     return count


# print(wands(tuple(map(int,input().split())),list(map(int,input().split()))))




# # def magic_wands(N, K, Powers):
# #     Powers.sort()
# #     To_Remove = 0
# #     while True:
# #         Power_Len = len(Powers)

# #         if Power_Len > 2:
# #             if (max(Powers) - min(Powers)) > K:
# #                 Powers = Powers[1:-1]
# #                 To_Remove += 2
# #             else:
# #                 break
# #         elif Power_Len in [1,2]:
# #             if (max(Powers) - min(Powers)) > K:
# #                 Powers = Powers[1:-1]
# #                 To_Remove += 1
# #         else:
# #             break
        
# #     return To_Remove


# # print(magic_wands(*map(int,input().split()),list(map(int,input().split()))))




def magic_wands(N, K, power_list):
    disteb_list = power_list.copy()
    if K == 0: return 0
    if N < 2: return 0
    if N == 2: 
        if abs(power_list[0] - power_list[-1]) > K: return 1
        else: return 0
    for disteb in power_list:
        if max(disteb_list) - min(disteb_list) > K:
            disteb_list.remove(disteb)

    if len(disteb_list) == len(power_list): return 0
    else: return len(disteb_list)
    


print(magic_wands(*map(int,input().split()),list(map(int,input().split()))))

# DEBUGGING
print(magic_wands(6,4, [7,4, 8, 1, 5, 9]))
print(magic_wands(4,10, [9,4,4,7]))
print(magic_wands(2,10, [50, 100]))





