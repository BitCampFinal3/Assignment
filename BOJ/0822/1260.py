import sys


def dfs(start, visited):
    visited += [start]
    for i in range(len(graph[start])):
        if graph[start][i] and i not in visited:
            visited = dfs(i, visited)
    return visited


def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        n = queue.pop(0)
        for i in range(len(graph[start])):
            if graph[n][i] and i not in visited:
                visited.append(i)
                queue.append(i)
    return visited


N, M, V = map(int, sys.stdin.readline().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start][end] = 1
    graph[end][start] = 1

print(*dfs(V, []))
print(*bfs(V))