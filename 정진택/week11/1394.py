#3/10
#문자열
#백준 1394번 암호: https://www.acmicpc.net/problem/1394
#접근방법: 문자 집합의 사이즈를 kSize라 하고 암호의 사이즈를 pSize라 했을 때,
#암호의 자릿수에 따라 kSize를 제곱해주며 답에 더해준다. 이를 하나의 식으로 썼었는데
#큰 지수 계산에 의해서 시간초과가 계속 났었고, for문으로 바꿔주어 문제를 해결하였다.

from sys import stdin 
keys = stdin.readline().rstrip()  # 암호로 사용할 수 있는 문자
mp = {char: i+1 for i, char in enumerate(keys)}
pw = stdin.readline().rstrip()  # 암호
MOD = 900528
ans = 0

kSize = len(keys) # 문자 집합 크기
pSize = len(pw)  # 암호 크기

for i in range(1, pSize): # 암호 자릿수 크기만큼 ans값 조정
    ans = (ans + kSize) % MOD 
    kSize = (kSize * len(keys)) % MOD

kSize = 1

for i in range(pSize-1, -1, -1): # 암호 각 자릿수의 가중치만큼 ans값 조정
    t = ((mp[pw[i]] - mp[keys[0]]) % MOD * kSize) % MOD
    ans = (ans + t) % MOD
    kSize = (kSize * len(keys)) % MOD

print((ans + 1) % MOD)

# 실패코드

# from sys import stdin  

# keys = stdin.readline().rstrip()
# answer = stdin.readline().rstrip()

# dic = {}
# res = 0
# kLength = len(keys)
# aLength = len(answer)

# for i in range(kLength):
#     dic[keys[i]] = i+1

# for i in range(aLength-1, -1, -1):
#     res = (res + (dic[answer[i]] * (kLength ** (aLength-i-1)) % 900528 )% 900528) % 900528

# # for i in range(aLength):
#     # res += dic[answer[i]] * kLength ** (aLength-i-1)

# print(res)
