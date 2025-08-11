n, m = map(int, input().split())
result = []

def backtrack():
    if len(result) == m: #m개를 골라서 출력
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, n+1): #고른m개 중에 1~n개 중에 숫자 출력
        if i not in result:
            result.append(i)
            backtrack() #백트래킹의 재귀
            result.pop() #마지막 숫자 제거 (처음으로 다시 돌아가기 위함)
backtrack()