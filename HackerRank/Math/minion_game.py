# Kevin and Stuart want to play the 'The Minion Game'.
# Game Rules
# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels. 
# The game ends when both players have made all possible substrings. 








def minion_game(string):
    vowels = 'AEIOU'
    slen = len(string)
    Stuart, Kelvin = 0, 0
    for i in range(slen):
        if string[i] in vowels:
            Kelvin+= slen-i
        else:
            Stuart+= slen-i
    
        
    if Stuart > Kelvin: print(f"Stuart {Stuart}")
    elif Stuart < Kelvin: print(f"Kevin {Kelvin}")
    else: print(f"Draw")
    
    
        
if __name__ == '__main__':
    s = input()
    minion_game(s)