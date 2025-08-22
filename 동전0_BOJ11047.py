n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.reverse()

count=0
for i in coins:
    if k==0:
        break
    count += (k//i)
    k %= i
    
print(count)