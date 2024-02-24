from sys import stdin 

n, m = map(int, stdin.readline().split())
ms = list(map(int, stdin.readline().split()))
cs = list(map(int, stdin.readline().split()))

length = sum(cs)
dp = [[0 for _ in range(length + 1)] for _ in range(n+1)]
ans = float('inf')
for i in range(1,n+1):
    mi,ci = ms[i-1], cs[i-1]
    for j in range(length+1):
        dp[i][j] = dp[i-1][j]
    for j in range(ci, length+1):
        dp[i][j] = max(dp[i-1][j-ci] + mi, dp[i][j])
        if dp[i][j] >= m:
            ans = min(ans,j)
print(ans)
