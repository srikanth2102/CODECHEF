#https://www.codechef.com/START7C/problems/CEILSUM
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if(a==b):
        print(0)
        continue;
    else:
        x=min(a,b)+1
    if((b-x)%2==0):
        t1=(b-x)//2
    else:
        t1=((b-x)//2)+1
    if((x-a)%2==0):
        t2=(x-a)//2
    else:
        t2=((x-a)//2)+1
    print(t1+t2)
