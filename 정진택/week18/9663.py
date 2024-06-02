#6/2
#백트래킹
#백준 9663번 N-Queen: https://www.acmicpc.net/problem/9633
#접근방법
#퀸을 하나 놓을 때마다 같은 column 과 같은 대각선(y=x, y=-x)상의 점들을
#모두 방문처리하며 백트래킹해준다.


def n_queen(r): # r은 행을 나타낸다.
    global n, cnt 

    if r == n:
        cnt += 1
        return 
    
    for c in range(n): # c는 열을 나타낸다.
        if not cols[c] and not yequalx[r+c] and not yequal_x[n-1+r-c]:
            cols[c] = True
            yequalx[r+c] = True
            yequal_x[n-1+r-c] = True 
            n_queen(r+1)
            cols[c] = False
            yequalx[r+c] = False
            yequal_x[n-1+r-c] = False


n = int(input())

# 같은 열 방문처리
cols = [False]*n
# 같은 x=y 방문처리
yequalx = [False]*(2*n-1)
# 같은 x=-y 방문처리
yequal_x = [False]*(2*n-1)

cnt = 0

n_queen(0)
print(cnt)



# cnt = 0
# row = [0] * n

# def is_not_visited(r):
#     for c in range(r):
#         if row[r] == row[c] or abs(row[r] - row[c]) == abs(r - c):
#             return False
    
#     return True

# def n_queens(r):
#     global ans
#     if r == n:
#         ans += 1
#         return

#     else:
#         for c in range(n):
#             row[r] = c
#             if is_not_visited(r):
#                 n_queens(r+1)

# n_queens(0)
# print(cnt)
