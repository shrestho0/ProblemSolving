

'''
Type 1: RXGY, where X and Y are integers. 
X : Roll number
Y : Group identifier

Type 2: PQ,
P : Group identifier 
Q : Roll number.

Output: Group, Roll

'''

def roll_identifier(roll: str):
    roll = roll.upper()
    # Type 01
    if 'R' in roll and 'G' in roll:
        r_index = roll.index("R")
        g_index = roll.index("G")
        return roll[g_index+1:] +' '+ roll[r_index+1: g_index]

    # Type 02
    else:
        group = "".join(x for x in roll if x.isalpha())
        rolli = "".join(x for x in roll if x.isdigit())
    return group +' '+ rolli
    

def multi_roll_identifier(n):
    for i in range(1, n+1):
        print(f"Case {i}: {roll_identifier(input())}")

multi_roll_identifier(int(input()))
# 5
# R65G45
# R106G7
# ABC21
# BATMAN0040
# R02G001