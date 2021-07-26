# https://www.codechef.com/START6C/problems/CRICRANK
t=int(input())
for i in range(t):
    a1,b1,c1=map(int,input().split())
    a2,b2,c2=map(int,input().split())
    p1=0
    p2=0
    if(a1>a2):
        p1+=1
    else:
        p2+=1
    if(b1>b2):
        p1+=1
    else:
        p2+=1
    if(c1>c2):
        p1+=1
    else:
        p2+=1
    if(p1>p2):
        print("A")
    else:
        print("B")
