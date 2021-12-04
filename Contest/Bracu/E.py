



# # # # # def ebox_delivery(box_count: int, boxes: tuple) -> int:
# # # # #     boxes.sort()
# # # # #     total_box = box_count
# # # # #     boxes = [x**3 for x in boxes]
    
# # # # #     for idx in range(total_box-1):
# # # # #         if boxes[idx] < boxes[idx+1]:
# # # # #             total_box -= 1

# # # # #     return total_box









# # # def box_delivery(box_count, boxes):
# # #     extra = [boxes.count(x) for x in boxes]
# # #     return sorted(extra, reverse=True)[0]
        

# # # # def ebox_delivery(box_count: int, boxes: list) -> int:
# # # #     if box_count == 0: return 0
# # # #     if box_count == 1: return 1
# # # #     boxes.sort()
# # # #     packed = []
# # # #     total = 0
# # # #     for i in range(box_count-1):
# # # #         if boxes[i] < boxes[i+1]:
# # # #             packed.append(boxes[i])
# # # #             total += 1

# # # #     return box_count - len(packed)

# # # def box_delivery(box_count, boxes):
# # #     return sorted([boxes.count(x) for x in boxes])[-1]

# # # input()
# # # print(box_delivery(0, list(map(int, input().split()))))

# # # print(box_delivery(3, [1,2,3]))
# # # print(box_delivery(3, [1,1,3]))
# # # print(box_delivery(4, [2, 2, 3, 1]))




# # # def box_delivery(boxes):
# #     # return sorted([boxes.count(x) for x in boxes])[-1]

# input()
# x = tuple(x for x in input().split())
# c = (x.count(i) for i in x)
# print(max(c))




# def magic_wands(N, K, power_list):
#     disteb_list = power_list.copy()
#     if K == 0: return 0
#     if N < 2: return 0
#     if N == 2: 
#         if abs(power_list[0] - power_list[-1]) > K: return 1
#         else: return 0
#     for disteb in power_list:
#         if max(disteb_list) - min(disteb_list) > K:
#             disteb_list.remove(disteb)

#     if len(disteb_list) == len(power_list): return 0
#     else: return len(disteb_list)


# print(magic_wands(*map(int,input().split()),list(map(int,input().split()))))


input()
# x = list(x for x in input().split())
x = input().split()
print(max(x.count(i) for i in x))