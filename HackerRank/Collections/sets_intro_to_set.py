

 
# #@ Introduction to sets
# ## Leaning part


# print(set())
# print(set('HackerRank'))
# print(set([1,2,2,3,2,1,3,2,2,4,4,2,0]))
# print(set(set(['H', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k'])))
# print(set(enumerate(['H', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k'])))



def average(array):
    array = set(array)
    return f'{sum(array)/len(array):.3f}'

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
