n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(k+1)] for _ in range(n)]
#초기값 설정시 주의!!
fwt, fwm, frt, frm = arr[0]
dp[0][fwt] = fwm
if fwt == frt:
    frm = max(frm, fwm)
dp[0][frt] = frm
for i in range(1, n):
    wTime, wMoney, rTime, rMoney = arr[i]
    for j in range(k, -1, -1):
        if j-wTime >= 0 and dp[i-1][j-wTime] > 0:
            dp[i][j] = max(dp[i][j], wMoney+dp[i-1][j-wTime])
        if j-rTime >= 0 and dp[i-1][j-rTime] > 0:
            dp[i][j] = max(dp[i][j], rMoney+dp[i-1][j-rTime])
ans = max(dp[n-1])
print(ans)
