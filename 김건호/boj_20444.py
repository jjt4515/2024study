import sys
n,k=map(int,sys.stdin.readline().split())

d=(n+2)**2-4*k
if d<0 :
    print("NO")
else : #d>=0
    if int(d**0.5)**2==d:
        sol1=((n+2)+d**(0.5))/2
        sol2=((n+2)-d**(0.5))/2
        if sol1>=1 and sol2>=1 :
            if sol1.is_integer() and sol2.is_integer():
                print("YES")
            else :
                print("NO")
        else :
            print("NO")
    else :
        print("NO")
