

with open('input1.txt', 'r') as f:
    sFuckinList =[]
    for sList in f.read().split('\n\n'):
        sListSum = sum(map(int, sList.split('\n')))
        sFuckinList += [sListSum]
    print(sFuckinList, 'Elf', sFuckinList.index(max(sFuckinList))+1,max(sFuckinList))