import sys,math
from collections import deque

k=(int)(input())
w,h=map(int,sys.stdin.readline().split())
table=[0 for _ in range(h)]

for i in range(h):
    table[i] = list(map(int,sys.stdin.readline().split()))

dx=[-1,0,1,0]
dy=[0,1,0,-1]
horse_dx=[-2,-1,1,2,2,1,-1,-2]
horse_dy=[1,2,2,1,-1,-2,-2,-1] 
queue=deque()
queue.append([0,0,k]) #pos_x,pos_y,remain_count, remain_count
visited = [[[math.inf]*(k+1) for _ in range(w)] for _ in range(h)]
visited[0][0][k]=0
while queue : 
    top=queue.popleft()
    pos_x=top[0]
    pos_y=top[1]
    remain_count=top[2]
    
    if table[pos_x][pos_y]==1 : #장애물
        continue
    else :
        if pos_x==h-1 and pos_y==w-1 :
            print(visited[pos_x][pos_y][remain_count])
            sys.exit()
        
        for i in range(4) :
            if (pos_x+dx[i]>=0 and pos_x+dx[i]<h) and (pos_y+dy[i]>=0 and pos_y+dy[i]<w) :
                if visited[pos_x+dx[i]][pos_y+dy[i]][remain_count] > visited[pos_x][pos_y][remain_count]+1 : 
                    queue.append([pos_x+dx[i], pos_y+dy[i], remain_count])    
                    visited[pos_x+dx[i]][pos_y+dy[i]][remain_count]=visited[pos_x][pos_y][remain_count]+1
        if remain_count>0 :
            for i in range(8) :
                if (pos_x+horse_dx[i]>=0 and pos_x+horse_dx[i]<h) and (pos_y+horse_dy[i]>=0 and pos_y+horse_dy[i]<w) :
                    if visited[pos_x+horse_dx[i]][pos_y+horse_dy[i]][remain_count-1] > visited[pos_x][pos_y][remain_count]+1 :
                        queue.append([pos_x+horse_dx[i], pos_y+horse_dy[i], remain_count-1])
                        visited[pos_x+horse_dx[i]][pos_y+horse_dy[i]][remain_count-1]=visited[pos_x][pos_y][remain_count]+1
print(-1)
