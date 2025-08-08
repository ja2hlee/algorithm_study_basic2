k, n = map(int, input().split())
LAN = list(int(input()) for _ in range(k))
    
start, end = 1, max(LAN)

while start <= end:
    line = 0
    mid = (start+end)//2
    
    
    for i in LAN:
        line += i//mid #mid로 만들 수 있는 핸선의 길이
        
    if line >= n: #더 만들 수 있으면 더 만들도록 함
        start = mid+1
    else:
        end = mid-1 #부족하면 길이를 줄임
print(end) 