#4/28
#브루트포스
#백준 1007번 벡터매칭: https://www.acmicpc.net/problem/1007
#접근방법: n 개 중 n/2개를 선택하고 반은 시작점, 반은 끝점으로 함.
#combination으로 모든 조합의 경우를 보며 끝점 좌표 - 시작점 좌표를 하여 벡터의 
#좌표를 계산 후 최소 길이를 찾음.

import itertools

t = int(input())
for _ in range(t):
    n = int(input())
    dots = []
    total_x, total_y = 0,0

    for _ in range(n):
        x, y = map(int, input().split())
        total_x += x
        total_y += y
        dots.append([x,y])

    ans = float('inf')
    comb = list(itertools.combinations(dots, n//2))
    for com in comb[:len(comb)//2]:
        x1, y1 = 0, 0 
        for x, y in com:
            x1 += x
            y1 += y
        x2, y2 = total_x - x1, total_y - y1

        vector = ((x2-x1)**2 + (y2-y1)**2)**(0.5)
        ans = min(ans, vector)
    print(ans)
    
