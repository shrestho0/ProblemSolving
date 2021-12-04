





for i in range(5):
    row = tuple(int(x) for x in input().split())
    for j in range(5):
        if row[j] == 1:
            print(abs((2-i)) + abs((2-j)))
            break
        
# 0 0 0 0 0
# 0 0 0 0 1
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0




# print(*all_matrix, sep="\n")
# print()
# for i in range(len(all_matrix)):
#     print(all_matrix[i])

# print()
# for i in range(len(all_matrix)-1): #Column 
#     for j in range(len(all_matrix)-1): #Row
#         pass
    
#     all_matrix[i], all_matrix[i+1] = all_matrix[i+1], all_matrix[i]
        
#         if 1 in all_matrix[i]: break
    
# print()
# print(*all_matrix, sep="\n")
    # all_matrix[i].reverse()
    # print()

    #     if all_matrix[2][2] == 1: break
    # all_matrix[i+1], all_matrix[i] = all_matrix[i], all_matrix[i+1]
    
# print(f"Swapped: {all_matrix}")
# for i in range(5):
#     arr = [int(x) for x in input().split()]
#     for j in range(5):
#         if arr[j] == 1:
#             print(abs(2 - i) + abs(2 - j))
#             exit
# all_matrix[2][2]
# 0 0 0 0 0
# 0 0 0 0 1
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0

# 0 0 0 0 0
# 0 0 0 0 1
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0



# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5