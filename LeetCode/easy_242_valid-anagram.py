def isAnagram(s, t):
    #aproach 1
    s = list(s)
    s.sort()
    t = list(t)
    t.sort()
    
    return s == t

    #aproach 2 worse one
    # s = list(s)
    # s.sort()
    # t = list(t)
    # t.sort()

    
    # for x,y in zip(s,t):
    #     if x != y:
    #         return False
        
    # return True
    
    
    
s = "anagram"; t = "nagaram"; print(isAnagram(s,t))
s = "rat"; t = "car"; print(isAnagram(s,t))
    