#https://www.codechef.com/problems/TABLET
t=int(input())
for i in range(t):
    n,b=map(int,input().split())
    l=[]
    for i in range(n):
        w,h,p=map(int,input().split())
        l.append((w*h,p))
    l.sort(reverse=1)
    flag=''
    for i in l:
        if(i[1]<=b):
            flag='pass'
            print(i[0])
            break;
    if(flag==''):
        print("no tablet")
