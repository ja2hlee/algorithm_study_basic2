from collections import deque

n,m,v = map(int, input().split())

#행렬 만들기
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

#DFS
def dfs(graph, v, visited):
    visited[v] = True #방문처리
    print(v, end=' ')
    
    for neighbor in range(1, len(graph)): #현재노드의 이웃노드 확인
        if graph[v][neighbor] == 1 and not visited[neighbor]: #확인 후 방문 안했으면
            dfs(graph, neighbor, visited) #재귀 호출
            
#BFS
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True #방문 처리
    
    while queue:
        v = queue.popleft() #큐에서 하나씩 꺼냄
        print(v, end=' ')
        
        for neighbor in range(1, len(graph)):
            if graph[v][neighbor] == 1 and not visited[neighbor]: #가보지 않은 곳
                visited[neighbor] = True
                queue.append(neighbor) #나중 방문을 위한 큐에 추가
                
#방문 리스트 행렬
visited_dfs = [False] * (n+1)
visited_bfs = visited_dfs.copy()

dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)