#https://www.codechef.com/START4C/problems/LAZYCHF
t=int(input())
for i in range(t):
    x,m,d=map(int,input().split())
    time=m*x
    if(m*x-x>d):
        print(x+d)
    else:
        print(m*x)
