#3/3
#기하학
#백준 1069번 집으로: https://www.acmicpc.net/problem/1069
#접근방법: 이동방법은 최대 점프 후 걷기, 점프만하기, 걷기만하기 세 경우로 나눌수있다.
#이는 집까지의 거리가 점프 거리보다 클때와 작을때 각각 식이 달라진다.

from sys import stdin  
import math 
x,y,d,t = map(int,stdin.readline().split())

distance = math.sqrt(x**2 + y**2) # 거리 구하기 

if distance >= d: #점프 거리보다 클때
    time = min(t*(distance//d) + distance % d, t * (distance // d + 1), distance)
    # 최대 점프 후 걷기, 점프만으로 가기, 걸어가기 
else: #점프 거리보다 작을때
    time = min(t + (d - distance), 2 * t, distance)
    # 최대 점프 후 뒤로 걷기, 점프만으로 가기, 걸어가기
print(time)
