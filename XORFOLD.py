# https://www.codechef.com/COOK130C/problems/XORFOLD
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    l=[]
    for i in range(n):
        temp=str(input())
        temp=list(temp)
        l.append(temp)
    c=0
    for i in range(n):
        for j in range(m):
            if(l[i][j]=='1'):
                c+=1
    if(c%2!=0):
        print("YES")
    else:
        print("NO")
