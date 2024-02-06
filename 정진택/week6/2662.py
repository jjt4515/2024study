#2/6
#dp, 배낭문제
#백준 2662번 기업투자: https://www.acmicpc.net/problem/2662
#접근방법: 2차원 배열 풀이법인데, 1차원 배열로도 풀이 가능
#dp 2차원 배열을 만들고, 현재 액수와 포함된 기업들에 따라 dp를 갱신한다.
#dp[i][j]에서 i는 현재 액수, j는 현재 투자할 기업을 나타내는데, 현재 기업에 몰빵할지,
#현재 기업에 투자를 안할지, 현재 기업과 다른 기업에 분산투자할지에따라 값을 변경해준다.

from sys import stdin    
n, m = map(int, stdin.readline().split())


money = [[0] * (m+1)]
for _ in range(n):
    money.append(list(map(int, stdin.readline().split())))

dp = [[0 for _ in range(m+1)] for _ in range(n+1)] # 총 이익 저장
path = [[[0 for _ in range(m+1)] for _ in range(m+1)] for _ in range(n+1)] # 각 기업에 투자한 액수 저장


for i in range(1, n+1): # 액수 별
    for j in range(1, m+1): # 기업 별
        dp[i][j] = max(dp[i][j-1], money[i][j]) #현재 기업에 몰빵 or 현재 기업 제외했을때 최대
        
        if dp[i][j] == money[i][j]: #현재 기업에 몰빵
            path[i][j][j] = i 
        else: #현재 기업 제외했을때 최대
            path[i][j] = path[i][j-1].copy()

        for k in range(1, i+1):
            if dp[i][j] < dp[k][j-1] + money[i-k][j]: #현재 기업에서 k만큼, 다른 기업들에 i-k만큼 분산투자 한 경우
                dp[i][j] = dp[k][j-1] + money[i-k][j] 
                path[i][j] = path[k][j-1].copy()
                path[i][j][j] = i - k
                
print(dp[n][m])
print(*path[n][m][1:])


