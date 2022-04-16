

def check_anagram(w1, w2):
    anagram = True
    if len(w1) == len(w2):
        for x in w1:
            if x in w2: anagram *= True
                
            else:
                anagram *= False
    else:
        anagram *= False
    
    
    return "Yes" if anagram else "No"



w1, w2 = input(), input()
print(check_anagram(w1, w2))
