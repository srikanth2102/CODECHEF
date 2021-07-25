#https://www.codechef.com/START7C/problems/CHSFORMT
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if(a+b<3):
        print(1)
    if(a+b>=3 and a+b<=10):
        print(2)
    if(a+b>=11 and a+b<=60):
        print(3)
    if(a+b>60):
        print(4)
