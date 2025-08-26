n = int(input())
m = int(input())

def dfs(graph, v, visited):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

# 그래프 초기화
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2) #양방향 표시
    graph[c2].append(c1)
    
visited = [False] * (n + 1)

dfs(graph, 1, visited) #1번에서 시작

#1번 제외하고 컴퓨터 수 세기
count=visited.count(True)-1
print(count)