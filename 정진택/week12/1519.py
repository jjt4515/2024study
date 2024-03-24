#3/21
#문자열, dp
#백준 1519번 부분 문자열 뽑기 게임: https://www.acmicpc.net/problem/1519
#접근방법: dp배열을 만들어 각 n에 대한 출력을 저장한다.
#n이 1의 자릿수인경우 고를수있는 진부분 문자열이 없으므로
#-1을 출력한다. n이 10인 경우 1일 고르면 상대가 패배하므로 1을 저장한다.
#그 이상의 숫자들은 반복문들을 통해 고를 수 있는 진부분 문자열을 가지고
#n에서 진부분 문자열을 뺀 수를 i라 할때 dp[i]가 -1이라면, 즉 하나의 진부분 문자열을
#선택했을때 상대가 패배한다면 그 수를 저장한다. 
#이 과정을 dp[n]까지 반복한 후 dp[n]을 출력한다.

n = int(input())
dp = [-1]*(n+1)
#초기값 설정
if n < 10:
    print(-1)
    exit()
dp[10] = 1
for i in range(11, n+1):
    arr = []
    s = str(i)

    #가능한 진부분 문자열 담기
    for j in range(len(s)):
        for k in range(j, len(s)):
            num = int(s[j:k+1])
            if num != 0 and num != i:
                arr.append(num)

    #오름차순으로 정렬
    arr.sort()

    #이 수를 골랐을때 상대가 패배한다면 고르고, 그런 수가 없으면 -1
    for j in range(len(arr)):
        if dp[i-arr[j]] == -1:
            dp[i] = arr[j]
            break 

print(dp[n])

