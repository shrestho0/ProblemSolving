



# # for (int i = 0; i < n; i++) {
# #     // Track number of elements swapped during a single array traversal
# #     int numberOfSwaps = 0;
    
# #     for (int j = 0; j < n - 1; j++) {
# #         // Swap adjacent elements if they are in decreasing order
# #         if (a[j] > a[j + 1]) {
# #             swap(a[j], a[j + 1]);
# #             numberOfSwaps++;
# #         }
# #     }
    
# #     // If no elements were swapped during a traversal, array is sorted
# #     if (numberOfSwaps == 0) {
# #         break;
# #     }
# # }

# arr = [4,3,1,2]

# for i in range(len(arr)):
#     # Track number of elements
#     number_of_swap = 0

#     for j in range(len(arr)-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#             number_of_swap += 1

#     if number_of_swap == 0:
#         break
# print(number_of_swap)



# n = input()
# arr = map(int, input().split())


# print(arr)
# #@TASKS
# import random 


# arr = [3, 2, 1]
# koto_bar = 0
# # arr = [random.randint(1, 100) for _ in range(10)]
# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
#             koto_bar+=1

# print(arr==sorted(arr))
# print(koto_bar)


# # Modified Version
# import random 


def koto_bar_swap(arr):
    koto_bar = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                koto_bar+=1

    return f'Array is sorted in {koto_bar} swaps.\n' + f'First Element: {arr[0]}\n' + f'First Element: {arr[-1]}'

print(koto_bar_swap([1,5,2,3,4]))