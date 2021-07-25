# https://www.codechef.com/START7C/problems/FODCHAIN
t=int(input())
for i in range(t):
    e,k=map(int,input().split())
    count=0
    while(e>0):
        count+=1
        e=e//k
    print(count)
