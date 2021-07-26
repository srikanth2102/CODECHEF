# https://www.codechef.com/JULY21C/problems/EITA
t=int(input())
for i in range(t):
    d,x,y,z=map(int,input().split())
    print(max(7*x,d*y+(7-d)*z))
    
