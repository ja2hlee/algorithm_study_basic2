n,s = map(int, input().split())
nums = list(map(int, input().split()))
count = 0
ans = [] #현재까지 선택한 수열을 저장하는 리스트

def backtrack(start):
    global count
    if sum(ans) == s and len(ans) > 0:
        count += 1
        
    for i in range(start, n):
        ans.append(nums[i])
        backtrack(i+1)
        ans.pop() 
        
backtrack(0)
print(count)