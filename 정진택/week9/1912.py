from sys import stdin   
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
dp = [0]*n
dp[0] = nums[0]
for i in range(1,n):
   dp[i] = max(dp[i-1]+nums[i], nums[i])
print(max(dp))
