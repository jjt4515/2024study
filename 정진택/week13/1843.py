#4/4
#소수판정
#백준 1843번 방정식: https://www.acmicpc.net/problem/1843
#접근방법
#A) y는 x보다 커야하므로 x가 1일때, y의 수는 n-2, x가 2일때, y의 수는 n-4..
#와 같은 규칙성을 가진다. 이를 시그마 (n - 2*k)로 표현하여 수학적으로 계산가능하고,
#다른 방법으로는 단순히 while문을 이용하여 계산가능하다.

#제약조건 B와 C에 대해서는 시간초과가 안나게 하는것이 중요한데, 이를 위해 n보다 작은 약수를 담는 리스트, n보다 작은 소수를 담는 리스트
#1부터 n까지의 수 중 어떤 수가 n의 약수인지, 또는 소수인지 판별을 위한 리스트를 만든다.

#B) n보다 작은 수 중 n의 약수를 검사한다. 이후 n의 약수들 중에서 반복문을 돌며 두 수를 합쳤을 때 
#n의 약수인지 판별하며 ans에 1씩 더해준다.

#C) n보다 작은 수 중 소수를 검사한다. 이후 소수들 중에서 반복문을 돌며 두 수를 합쳤을 때 소수인지 판별하며 ans에 1씩 더해준다.
#2부터 n까지 반복문을 돌며 k가 소수인지 판별할때, 2부터 k-1까지 나누면서 k가 소수인지 판별하면 시간복잡도가 O(N^2)이 되어 시간초과가 난다.
#약수의 성질에 의해 k가 a*b(a<b)일때 a는 항상 k의 제곱근보다 작거나 같으므로 2부터 k-1까지 나누는 것이 아닌 2부터 int(루트(k))까지 나눠도
#소수판별이 가능하다. 이때 시간복잡도는 O(N^(3/2))이 되어 시간초과가 나지 않는다.

import math

n = int(input())

# 제약조건 A
ans = 0
i = 1
# while문으로 해결
while True:
    a = n - 2*i
    if a <= 0:
        break
    ans += a
    i += 1

# 시그마 공식을 이용
# if n % 2 == 0:
#     ans = (n**2 // 4) - (n // 2)
# else:
#     ans = ((n-1)**2) // 4
print(ans)


# 제약조건 B
def is_prime(num): #소수 판별
    for k in range(2, int(math.sqrt(num)) + 1): # num을 k로 나누면서 소수판별시 루트(num)까지만 나눔
        if num % k == 0:
            return False
    return True

mans = 0
pans = 0

lst = [0 for _ in range(n+1)] # 현재 인덱스의 수가 n의 약수인지, 소수인지 혹은 둘다 해당하는지 저장
lst[1] = 1 #1은 항상 n의 약수

measure = [1]
primes = []
for i in range(2, n+1):
    if n % i == 0: #n의 약수이면 lst[i]에 1저장
       measure.append(i)
       lst[i] = 1
       if is_prime(i): #n의 약수이자 소수이면 lst[i]에 3저장
            primes.append(i)
            lst[i] = 3
    elif is_prime(i): #소수이면 lst[i]에 2저장
       primes.append(i)
       lst[i] = 2

mlen = len(measure)
plen = len(primes)

for i in range(mlen):
    for j in range(i, mlen):
        m = measure[i] + measure[j] # 두 약수 합이 약수면 출력값 1씩 증가
        if m <= n and lst[m] == 1 or m <= n and lst[m] == 3:
            mans += 1
print(mans)
 
for i in range(plen):
    for j in range(i, plen):
        p = primes[i] + primes[j] # 두 소수 합이 소수면 출력값 1씩 증가
        if p <= n and lst[p] == 2 or p <= n and lst[p] == 3:
            pans += 1
print(pans)

            
            
