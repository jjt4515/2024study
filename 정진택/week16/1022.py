#5/12
#구현
#백준 1022번 소용돌이 예쁘게 출력하기: https://www.acmicpc.net/problem/1022
#접근방법: 소용돌이를 그리면서 값들을 모두 2차원 배열에 넣으려면
#배열을 첨에 만들때 10001X10001의 사이즈로 만들어야해서 메모리초과 + 시간초과 남
#그래서 반복문으로 소용돌이를 동안 값이 입력 범위 내의 값일 때만 따로 작게 배열만들어서
#거기에 값을 넣음 

r1, c1, r2, c2 = map(int, input().split())
graph = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)] # 범위 내 배열
zero_count = (r2-r1+1) * (c2-c1+1) # graph 내 0 갯수(덜 채워진거 갯수)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

num = 1
row, col = 0,0
n = 1
direction = 1

while True:
    if zero_count <= 0: # graph 다 채워지면 멈춤
        break
    for _ in range(2):
        for _ in range(n):
            if r1 <= row <= r2 and c1 <= col <= c2: # 범위 내의 값일 때
                graph[row-r1][col-c1] = num # graph 채움
                max_num = num 
                zero_count -= 1
                
            row = row + dx[direction] 
            col = col + dy[direction]
            num += 1 # 값은 1씩 증가

        # 반시계로 방향 계속 바뀌도록    
        direction = (direction - 1) % 4
    n += 1
max_len = len(str(max_num)) # 가장 큰 수 자릿수
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(graph[i][j]).rjust(max_len), end=" ") # 자릿수도 맞춰서 출력
    print()
