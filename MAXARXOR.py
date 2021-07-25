# https://www.codechef.com/START7C/problems/MAXARXOR
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    if(k<2**n//2):
        print((2*k)*(2**n-1))
    else:
        k=2**n//2
        print((2*k)*(2**n-1))
