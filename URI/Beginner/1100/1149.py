



def Summing_Consecutive_Integers(listo: str):
    if len(listo) == 2:
        # listo.sort()
        return sum(range(listo[0], listo[0]+listo[1]))
    else:
        listo = [listo[0],listo[-1]]       
        # listo.sort()
        return sum(range(listo[0], listo[0]+listo[1]))

print(Summing_Consecutive_Integers(list(map(int, input().split()))))

'''

3 2
3 -1 0 -2 2

'''

