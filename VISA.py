# https://www.codechef.com/COOK130C/problems/VISA
t=int(input())
for i in range(t):
    x1,x2,y1,y2,z1,z2=map(int,input().split())
    c=0
    if(x2>=x1):
        c+=1
    if(y2>=y1):
        c+=1
    if(z2<=z1):
        c+=1
    if(c==3):
        print("YES")
    else:
        print("NO")
