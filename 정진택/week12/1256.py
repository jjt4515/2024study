from sys import stdin       
n,m,k = map(int, stdin.readline().split())
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

dp[0][0] = 0
for i in range(1, n+1):
    dp[i][0] = 1
for i in range(1, m+1):
    dp[0][i] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] #개수 저장

if dp[i][j] < k:
    print(-1)
    exit()

ans = ''
while n > 0 and m > 0: 
    front = dp[n-1][m]
    if front >= k: #앞이 a일때
        n -= 1
        ans += 'a' 
    else:
        m -= 1 #앞이 z일때
        ans += 'z'
        k -= front
ans += ('a' * n + 'z' * m)

print(ans)