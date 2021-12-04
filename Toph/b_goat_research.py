



def goat_research(n):
    given_notes = []
    for _ in range(n): given_notes.append(input().strip())
    new_notes = []
    for note in given_notes:
        a_count = note.count('a')
        if a_count % 2 != 0:
            note = note[:-1:]
            if note.count('a') == 0:
                note += 'aa'
        new_notes.append(note)
    
    max_string = len(max(new_notes))//2
    for note in new_notes:
        space = max_string - len(note)//2
        print(" "*space+note)


goat_research(int(input()))