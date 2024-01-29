#1/23
#dp
#백준 1229번 육각수: https://www.acmicpc.net/problem/1229
#접근방법: 육각수 공식은 변의 길이가 x일때, 점의 개수는 x(2x-1)이다.
#자연수 n이 주어질때, 처음에 n보다 작은 육각수 중에 가장 큰 육각수들을
#순서대로 빼주면 될줄 알았는데, 꼭 그렇다고 최소인 경우는 아님을 알고 dp를
#이용하였다. n보다 작은 육각수들을 모두 구해주고 n에서의 최소개수는 n-육각수에서의 최소개수 + 1
#임을 이용하여 dp를 갱신해주고 문제를 해결하였다.

INF = float('inf')
dp = [INF] * 1000001
dp[0] = 0
dp[1] = 1
n = int(input())


side = 1
cur = 0
hex = []

while cur <= n:
    cur = side * (2 * side - 1) # n = x(2x - 1)
    if cur <= n:
        hex.append(cur) #n보다 작은 육각수들 구함
    side += 1
    
for i in range(2, n+1):
    min_val = INF
    for h in hex: #i보다 작은 육각수들
        if h > i: 
            break
        dp[i] = min(dp[i], dp[i-h] + 1) #dp 갱신


print(dp[n])    

  

    