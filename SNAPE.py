#https://www.codechef.com/problems/SNAPE
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c1=(a**2+b**2)**0.5
    if(a>b):
        c2=(a**2-b**2)**0.5
    else:
        c2=(b**2-a**2)**0.5
    print(min(c1,c2),max(c1,c2))
