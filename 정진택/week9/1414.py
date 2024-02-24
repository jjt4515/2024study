#2/22
#문자열, 스패닝트리, 그래프이론
#백준 1414번 불우이웃돕기: https://www.acmicpc.net/problem/1414
#접근방법: 컴퓨터가 연결됨을 확인하기 위해 union find 알고리즘을 사용하였다.
#다솜이가 기부할 수 있는 랜선의 길이의 최댓값을 출력하기 위해서는
#컴퓨터를 연결할 때 최소의 랜선 길이를 사용해야하므로, heap을 이용해서
#랜선의 길이가 작은 것부터 연결해주었다. union-find를 통해
#이미 연결된 컴퓨터임을 확인했다면 ans에 길이를 더해주었다.


import heapq
from sys import stdin

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
    
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a 
    else:
        parent[a] = b

        
n = int(stdin.readline())
parent = [i for i in range(n)]

cons = [list(map(str, stdin.readline().rstrip())) for _ in range(n)]
heap=[]
ans = 0

for i in range(n):
    for j in range(n):
        if cons[i][j] == '0': #0일때
            heapq.heappush(heap, [0,i,j])
        else:
            if cons[i][j].islower(): #소문자일때
                length = ord(cons[i][j]) - ord('a') + 1
            else: #대문자일때
                length = ord(cons[i][j]) - ord('A') + 27
            heapq.heappush(heap, [length,i,j]) #힙에 랜선의 길이와 연결되는 컴퓨터 번호를 넣음

while heap:
    length, a, b = heapq.heappop(heap)
    
    if length == 0:
        continue
    if find(a) != find(b): #연결 안되어 있다면
        union(a,b) #연결
    else:
        ans += length

for i in range(n):
    if find(i) != 0: #모두 연결된 게 아니라면
        flag = 0
        print(-1)
        exit()

print(ans)
    
