#2/18
#백트래킹
#백준 1759번 암호 만들기: https://www.acmicpc.net/problem/1759
#접근방법: 부르트포스로 일일이 암호들을 찾기에는 시간초과가 날 것이라
#생각해서 백트래킹을 활용하였다.
#백트래킹과정에서 글자 수가 l만큼일때 암호가 될 수 있는지를 판별하고 맞다면 출력하였다.
 

vowel = ['a','e','i','o','u']
l, c = map(int, input().split())
words = sorted(list(map(str, input().split())))

def back_tracking(cnt, idx):
    vo, co = 0,0
    if cnt == l:
        for i in range(l):
            if answer[i] in vowel:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print("".join(answer))
        return 
    for i in range(idx, c):
        answer.append(words[i])
        back_tracking(cnt+1, i+1)
        answer.pop()

answer=[]
back_tracking(0,0)



