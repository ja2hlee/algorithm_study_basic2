n, m, k = map(int, input().split())

team = min(n//2, m, (n+m-k)//3)

print(team)