# https://www.codechef.com/COOK130C/problems/BALLOON
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    print(max(l.index(1),l.index(2),l.index(3),l.index(4),l.index(5),l.index(6),l.index(7))+1)
    
