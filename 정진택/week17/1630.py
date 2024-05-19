#5/19
#수학, 소수 판정
#백준 1630번 오민식: https://www.acmicpc.net/problem/1630
#접근방법: 최소공배수를 구하기위해 소인수 분해 후 각 소인수들 중 제곱수가 가장 큰 수들만 곱한다.

n = int(input())
visited = [False for _ in range(n+1)] #방문처리
ans = 1

for i in range(2,n+1): #n이하 자연수
    if visited[i]:  #합성수는 이미 방문처리 후 건너뜀(소수만 봄)
        continue

    multi = 1

    for j in range(i,n+1,i):  #i의 배수
        visited[j] = True  #합성수는 방문처리 
        cnt = 0
        tmp = j

        while tmp % i == 0:   #j를 i로 몇번 나눌수 있는지 봄 (j 안에 i가 몇 제곱이있는지 봄)
            tmp //= i
            cnt += 1
        multi = max(multi,cnt)

    for _ in range(multi):
        ans = (ans*i) % 987654321  #i의 multi제곱만큼 곱해줌

print(ans)
