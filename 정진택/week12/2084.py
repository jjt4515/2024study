#3/17
#그리디
#백준 2084번 차수열: https://www.acmicpc.net/problem/2084
#접근방법: 만약 차수의 합이 홀수라면 그래프를 만들 수 없다. 반대로 짝수라면 그래프를 만들 수 있다.
#차수열을 내림차순으로 정렬하여 차수가 큰 순서대로 정점들을 연결하면 
#남김없이 차수를 사용하여 그래프를 만들 수 있다.
#정점들을 연결하면서 차수열이 내림차순이 아니게 될 수 있다.
#이 때문에 반복 때마다 차수열을 정렬해준다.

from sys import stdin

n = int(stdin.readline())
degree = list(map(int, stdin.readline().split()))

graph = [[0 for _ in range(n)] for _ in range(n)]

# 차수의 합이 홀수면 그래프를 못 만든다.
if sum(degree) % 2 == 1: 
    print(-1)
    exit()

# 각 노드의 인덱스를 같이 넣어준다.
for i in range(n):
    degree[i] = [degree[i], i]

while True:
    # 차수열을 내림차순으로 정렬
    degree.sort(reverse=True)

    # 모든 차수를 사용하면 종료
    if degree[0][0] == 0:
        break 

    # 현재 노드의 다음 노드부터 탐색
    for i in range(1, n):
        
        # 차수가 0일 때
        if degree[0][0] == 0:
            break
        if degree[i][0] == 0:
            continue

        # 아직 그래프 연결이 안되어있다면 연결
        if graph[degree[0][1]][degree[i][1]] == 0:
            graph[degree[0][1]][degree[i][1]] = 1
            graph[degree[i][1]][degree[0][1]] = 1
            degree[i][0] -= 1
            degree[0][0] -= 1
        

output = '\n'.join(' '.join(map(str, row)) for row in graph)
print(output)
