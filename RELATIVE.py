# https://www.codechef.com/JULY21C/problems/RELATIVE
t=int(input())
for i in range(t):
    g,c=map(int,input().split())
    print(int((c*c)/(2*g)))
    
