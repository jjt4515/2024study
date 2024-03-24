from sys import stdin  
from collections import defaultdict
n,d,k,c = map(int, stdin.readline().split())
arr = [int(stdin.readline()) for _ in range(n)]
arr.extend(arr)
left = 0
right = k
dic = defaultdict(int)
dic[c] += 1
result = 0

for x in arr[left:right]:
    dic[x] += 1

while right < len(arr):
    result = max(result, len(dic))
    dic[arr[left]] -= 1
    dic[arr[right]] += 1
    if dic[arr[left]] == 0:
        dic.pop(arr[left])
    left += 1
    right += 1

print(result)