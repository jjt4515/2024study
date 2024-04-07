#4/3
#dfs,백트래킹
#백준 1405번 미친로봇: https://www.acmicpc.net/problem/1405
#접근방법: 간단한 그래프 순회이므로 패스

n, ep, wp, sp, np = map(int, input().split())
ep = ep / 100
wp = wp / 100
sp = sp / 100
np = np / 100
ps = [sp, ep, np, wp]

visited = [[0 for _ in range(29)] for _ in range(29)]

ans = 0

def dfs(depth, row, col, percent):
    global ans
    visited[row][col] = 1
    if depth == n:
        ans += percent
        return
    depth += 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nrow = row + dx[i]
        ncol = col + dy[i]
        
        if visited[nrow][ncol] == 1:
            continue
        else:
            p = percent * ps[i]
            dfs(depth, nrow, ncol, p)
            visited[nrow][ncol] = 0
        

dfs(0, 14, 14, 1)
print(ans)