n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False]*n
result = []

def backtrack():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    prev = 0 #이전에 사용한 값 기억하도록 변수에 저장
    for i in range(n):
        if not visited[i] and nums[i] != prev: #(1 9) (1 9)와 같은 중복 불가 처리
            visited[i]=True #방문한 인덱스는 False->True로 변경
            result.append(nums[i])
            prev = nums[i] #같은 깊이에선 마지막으로 선택한 값을 저장하는 역할
            backtrack()
            visited[i]=False #다시 되돌아가게 바꿔줌
            result.pop()

backtrack()