# https://www.codechef.com/problems/TRAINWT
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    sum1=sum(l)
    q=int(input())
    for i in range(q):
        s,e,w=map(int,input().split())
        sum2=(e-s+1)*w
        sum1+=sum2
    print(sum1)
