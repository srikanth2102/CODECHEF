#https://www.codechef.com/problems/BEGGASOL
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    gas=l[0]
    l[0]=0
    i=1
    dist=0
    while(gas!=0):
        dist+=1
        gas-=1
        gas+=l[i]
        l[i]=0
        i=i+1
        if(i==len(l)):
            i=0
    print(dist)
