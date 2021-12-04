import re

jinis = input()
pattern = input()
all_indices = []
if not re.search(pattern, jinis):
    print((-1,-1))
else:
    for i in range(len(jinis)-len(pattern)-1):
        notun_jinis = jinis[i:]
        indices = re.search(pattern, notun_jinis)
        startx = indices.start()+i
        endx = startx+len(pattern)-1
        done_indices = (startx, endx)
        if done_indices not in all_indices:
            all_indices.append(done_indices)
        if endx == len(jinis)-1:
            break
        
    
    if len(all_indices) != 0:
        for el in all_indices:
            print(el)
