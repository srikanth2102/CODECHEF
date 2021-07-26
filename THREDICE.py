# https://www.codechef.com/START6C/problems/THREDICE
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    chance=6-(x+y)
    if(chance<=0):
        print(0)
    else:
        print(chance/6)
