# https://www.codechef.com/LTIME96C/problems/TWINGFT
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    cheff,chefl,twinf,twinl=0,0,0,0
    for i in range(k):
        cheff=cheff+max(l)
        twinf=twinf+max(l)
        l.remove(max(l))
        chefl+=max(l)
        twinl=max(l)
        l.remove(max(l))
    twinl+=max(l)
    chefl+=max(l)
    print(max(chefl,cheff))
