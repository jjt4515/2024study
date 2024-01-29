#1/17
#dp, bfs
#백준 14226번 이모티콘: https://www.acmicpc.net/problem/14226
#접근방법: 최소 연산의 수를 구해야 하므로 dp를 이용한다. 
#이때 만들어지는 dp배열은 화면에 있는 이모티콘과 클립보드에 있는 이모티콘 수를
#인덱스로 하는 이차원 배열이다. 연산이 세 종류이므로 각 연산을 거치며
#dp를 갱신해줘야하는데 이를위해서 dfs를 이용한다.
#deque를 통해 bfs를 돌며 dp 배열의 값을 앞에서부터 변경해준다.
#그냥 dp로는 못푼다 삭제 기능 때문에 bottom up 방식 안됨

from sys import stdin    
from collections import deque 

n = int(stdin.readline())
q = deque()
dp = [[-1]*(n+1) for _ in range(n+1)]

q.append((1, 0))
dp[1][0] = 0

while q:
    s,c = q.popleft()
    #-1은 방문 안됐다는 뜻
    #이모티콘 복사하기
    if dp[s][s] == -1: 
        dp[s][s] = dp[s][c] + 1
        q.append((s,s))
    #이모티콘 붙여넣기
    if s+c <= n and dp[s+c][c] == -1:
        dp[s+c][c] = dp[s][c] + 1
        q.append((s+c,c))
    #이모티콘 삭제하기
    if s - 1 >= 0 and dp[s-1][c] == -1:
        dp[s-1][c] = dp[s][c] + 1
        q.append((s-1, c))

ans = float('inf')
for i in range(1, n):
    if dp[n][i] != -1 and ans > dp[n][i]:
        ans = dp[n][i]
print(ans)
