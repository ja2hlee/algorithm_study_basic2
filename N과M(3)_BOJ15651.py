n, m = map(int, input().split())
result = []

def backtrack():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, n+1):
        result.append(i) #선택
        backtrack() #백트래킹핵심: 재귀
        result.pop() #마지막 제거해서 원래 상태 만들기

backtrack()