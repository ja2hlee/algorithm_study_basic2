from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x) #촌수(부모-자식)간 양방향
    
def bfs(a, b):
    visited = [False]*(n+1)
    queue = deque([(a, 0)])
    visited[a] = True
    
    while queue:
        current, dist = queue.popleft()
        if current == b:
            return dist
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, dist+1))
    return -1

print(bfs(a, b))