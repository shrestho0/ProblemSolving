



def byangs_add(n1, n2):
    no_carry = True
    n1 = [int(x) for x in n1]
    n2 = [int(x) for x in n2]

  
    for x,y in zip(n1[::-1], n2[::-1]):
        if x+y > 9: 
            no_carry *= False
            break

    return "No" if no_carry else "Yes"
    


print(byangs_add(*map(str, input().split()))) 