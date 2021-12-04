

def test_case(N,CPUL, MEML):
    problems = []
    for _ in range(N):
        nDiff, nCPU, nMEM = map(int, input().split())
        if nDiff != 0: 
            problems.append('WA')
        elif nCPU > CPUL: 
            problems.append('CLE')
        elif nMEM > MEML:
            problems.append('MLE')
    
    return problems[0] if problems else "AC"


N, CPUL, MEML = map(int, input().split())
print(test_case(N, CPUL, MEML))


    
