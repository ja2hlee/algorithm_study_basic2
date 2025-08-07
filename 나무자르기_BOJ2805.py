n, m = map(int, input().split())
tree= list(map(int, input().split()))
start, end = 1, max(tree) #이진탐색 검색 범위 설정

while start <= end:
    total = 0
    mid = (start+end)//2
    
    for i in tree:
        if i > mid:
            total += i-mid
        
    if total >= m: #나무를 많이 잘랐음, 더 적게 필요 -> 절단 높이를 높임
        start = mid+1
    else:
        end = mid-1 #적게 잘라서 더 많은 나무 필요 -> 절단 높이를 낮춤
print(end) #조건을 만족한 절단기의 높이 