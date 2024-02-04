#1/30
#dp
#백준 1823번 수확: https://www.acmicpc.net/problem/1823
#접근방법: 양 끝에서부터 수확할 수 있기 때문에 처음에 그리디로 접근하려 하였다.
#그런데 그리디로 접근할 경우, 작은 수부터 처리한다고해서 최대 이익이 나오는것이 아니므로 답을 구할 수 없다.
#그래서 dp를 이용하고자 하였고, dp 2차원 배열을 만들어 left와 right 수확한 양에 따라 최댓값을 갱신해주었다.


n = int(input())
v = [int(input()) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]

res = 0
for i in range(1, n+1):
    for left in range(0, i+1):
        right = i-left
        #인덱스 벗어나는거 대비
        if left == 0:
            dp[left][right] = dp[left][right-1] + i*v[-right]
        elif right == 0:
            dp[left][right] = dp[left-1][right] + i*v[left-1]

        #실제 점화식
        else:
            dp[left][right] = max(dp[left-1][right] + i*v[left-1], dp[left][right-1] + i*v[-right]) #왼쪽 또는 오른쪽 하나 덜 수확했을때의 최댓값 + 현재 얻는 이익
        
        if i==n:
            res = max(res, dp[left][right]) 

print(res)

