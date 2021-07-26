#https://www.codechef.com/COOK129C/problems/MARARUN
try:
    t=int(input())
    for i in range(t):
        D,d,A,B,C=map(int,input().split())
        dist=D*d
        if(dist<10):
            print(0)
            continue;
        if(dist>=42):
            print(C)
            continue;
        if(dist>=21):
            print(B)
            continue;
        if(dist>=10):
            print(A)
            continue;
except EOFError:
    pass;
