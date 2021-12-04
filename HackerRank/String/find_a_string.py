def count_substring(string, sub_string):
    count = 0
    string_len, sub_len = len(string), len(sub_string)
    for i in range(string_len):
        if sub_string == string[i:i+sub_len]:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)



# ABCDCDC
# CDC


# i -> i+len(len)



# for 

import re

string = "ABCDCDC"
sub_string = "CDC"
string_len = len(string)
sub_st_len = len(sub_string)

count = 0
for i in range(len(string)):
    if sub_string == string[i:i+sub_st_len]:
        count+=1