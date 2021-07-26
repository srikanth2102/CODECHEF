# https://www.codechef.com/LTIME97C/problems/CHFRICH
t=int(input())
for i in range(t):
    a,b,x=map(int,input().split())
    print(int((b-a)/x))
