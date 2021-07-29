#https://www.codechef.com/LTIME95B/problems/CCHEAVEN
t=int(input())
for i in range(t):
    n=int(input())
    s=str(input())
    good=0
    bad=0
    flag=''
    for i in s:
        if(i=='1'):
            good+=1
        else:
            bad+=1
        if(good>=bad):
            print('YES')
            flag='pass'
            break;
    if(flag!='pass'):
        print("NO")
