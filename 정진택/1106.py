#1/7
#dp
#백준 1106번 호텔: https://www.acmicpc.net/problem/1106
#접근방법: dp를 이용하여 문제를 해결한다. dp 배열을 만들고
#각 입력마다 갱신을 시켜주는데, dp의 각 인덱스는 얻는 고객 수, 각 인덱스에 해당하는
#값은 드는 비용을 의미한다. 각 입력별 고객수의 배수에 해당하는 인덱스의 값을 이전 값과 
#비교하여 갱신시켜준다. 문제에서 적어도 c명 늘려야 한다고 했으므로, c명 이상 늘려도 되는데, c 명
#보다 c 명 이상 늘리는게 최소 비용일 때도 있다. 그런 경우도 고려해주기 위해 dp배열의 크기를
#c가 아니라 거기에 100을 더한 수가 최대 인덱스가 되도록 한다.

from sys import stdin
c, n = map(int, stdin.readline().split())
lst = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [float("inf") for _ in range(c+100)]
dp[0] = 0

for cost, num in lst:
    for i in range(num, c+100):
        dp[i] = min(dp[i-num] + cost, dp[i])
print(min(dp[c:]))