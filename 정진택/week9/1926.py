from sys import stdin   
from collections import deque
n, m = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

def dfs(x,y):
    res = 1
    graph[x][y] = 0
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    stack = deque()
    stack.append([x,y])
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                stack.append([nx,ny])
                graph[nx][ny] = 0
                res += 1
    return res

cnt = 0
ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1
            ans = max(dfs(i,j), ans)
print(cnt)
print(ans)
