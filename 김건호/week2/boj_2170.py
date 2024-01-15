import sys

n=(int)(input())
lines=[]
for _ in range(n) :
    s,e = map(int ,sys.stdin.readline().split())
    lines.append((s,e))

lines.sort() #시작 기준으로 정렬
start=0
end=0
answer=0
for line in lines :
    if start==0 and end==0 :
        start = line[0]
        end=line[1]
    else : #맨 처음이 아니라면 
        new_line_start=line[0]
        new_line_end=line[1]
        if end>=new_line_start : 
            if new_line_end >end :
                end=new_line_end
        else :
            answer+=end-start
            start = new_line_start
            end= new_line_end

print(answer+(end-start))
