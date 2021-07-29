#https://www.codechef.com/problems/MULARR
t=int(input())
for i in range(t):
    n=int(input())
    pdt=1
    l=list(map(int,input().split()))
    for i in l:
        pdt*=i
    print(pdt)
