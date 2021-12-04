


# string = "I love python3".split()
# # Using Join Method
# string = "_".join(string)
# print(string)








def split_and_join(line):
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)