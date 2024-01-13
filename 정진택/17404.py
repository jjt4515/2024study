#1/9
#dp
#백준 17404번 RGB거리 2: https://www.acmicpc.net/problem/17404
#접근방법: dp배열을 만드는데, 이 배열은 이차원 배열이고 
#행의 개수는 입력 개수 n개이고, 크기가 3인 각 행은 r,g,b로 색칠했을때 
#최소 비용을 각각의 원소에 나타낸다. 이제 반복문을 돌며 dp의 각 행의 원소들을 갱신해주는데, 
#각각 r,g,b를 칠했을때 드는 비용에 그 전 dp에서 다른 색깔로 칠했을때 비용 중 최소값을 더해준다.
#이렇게 하는 이유는 색깔이 연달아 나타나면 안된다는 조건 때문이고, 마지막과 첫번째에도 연달아 나타나면
#안되기때문에 첫번째에서 r,g,b를 칠한 각각의 경우에 대해서 최소값을 구해주고, 마지막과 첫번째에 칠한 색이
#안겹치는 조건 하에 최종 최소값을 갱신해준다. 

from sys import stdin

INF = float("inf")
n = int(stdin.readline())
input_rgb = [list(map(int, stdin.readline().split())) for _ in range(n)]


res = INF
for i in range(3):
    dp = [[INF, INF, INF] for _ in range(n)]
    dp[0][i] = input_rgb[0][i]

    for j in range(1, n):
        dp[j][0] = input_rgb[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = input_rgb[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = input_rgb[j][2] + min(dp[j-1][0], dp[j-1][1])

    dp[n-1][i] = INF
    res = min(res, min(dp[n-1]))

print(res)