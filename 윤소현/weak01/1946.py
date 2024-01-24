
import sys
input = sys.stdin.readline

test_case = int(input())
for i in range(test_case):
    applicant = int(input())
    data = []

    for _ in range(applicant):
        paper, interview = map(int, input().split())
        data.append((paper, interview))
    data.sort()

    new = 1
    winner = data[0][1]
    for paper, interview in data:
        if interview < winner:
            winner = interview
            new += 1

    print(new)
    
