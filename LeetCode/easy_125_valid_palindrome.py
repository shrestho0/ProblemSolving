def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    
    # s = s.replace(" ", "").replace(",","")

    # # remove not alpha:
    # new_str = ""
    # for c in s:
    #     new_str+= c.lower() if c.isalnum() else ""
    
    # s = new_str
    # slen =len(s)
    
    # i = 0
    # j = slen - 1
    
    # while i < j:
    #     if s[i]!=s[j]:
    #         # print(s[i], s[j])
    #         return False
    #     i += 1
    #     j -= 1
        
    # return True
    
    

    x = list(filter(lambda strx: strx.isalnum(), s.lower()))
    mid = (len(x))//2
    
    if not x or x[:mid] == x[mid+1:][::-1]:
        return True

    return False


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
