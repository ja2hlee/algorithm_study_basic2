from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, h, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] > h:
                    visited[nx][ny] = True
                    q.append((nx, ny))

max_height = max(map(max, graph))
answer = 0

for h in range(max_height + 1):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > h:
                bfs(i, j, h, visited)
                cnt += 1
    answer = max(answer, cnt)

print(answer)