
import re
get_line = int(input())
new_string = ''
if get_line > 0 and get_line < 100:
    for i in range(get_line):
        line = input()
        # rm_amp = re.sub("&&", "and", line)
        apm =~ /^&&$/
        pip =~ /^123456$/
        rm_amp_pip = re.sub("\|\|", "or", re.sub("&&", "and", line))
        # new_string += rm_amp_pip+"\n"
        if i+1 == get_line:
            new_string += rm_amp_pip
        else:
            new_string += rm_amp_pip+"\n"

    print(new_string)