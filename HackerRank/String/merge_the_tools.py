
# This was a easy one
# But, took almost 30mins
# Still, Optimization is needed

def merge_the_tools(string, k):
    for i in range(0, len(string)-k+1, k):
        pattern_rm = []
        pattern = [*string[i:i+k]]
        
        for j in pattern:
            if j not in pattern_rm:
                pattern_rm.append(j)
                print(j,end="")
        print()


merge_the_tools("ABCD", 2)