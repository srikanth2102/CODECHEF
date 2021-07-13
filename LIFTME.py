#https://www.codechef.com/problems/LIFTME
t=int(input())
for i in range(t):
    n,q=map(int,input().split())
    current=0
    dist=0
    for i in range(q):
        start,end=map(int,input().split())
        dist+=abs(current-start)
        current=start
        dist+=abs(current-end)
        current=end
    print(dist)
