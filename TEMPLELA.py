# https://www.codechef.com/problems/TEMPLELA
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if(l[0]!=1 or l[n-1]!=1):
        print('no')
        continue;
    if(n%2==0):
        print('no')
        continue;
    centre=n//2
    print(centre)
    for i in range(centre):
        try:
            if(l[i+1]-l[i]!=1):
                flag='fail'
                break;
        except IndexError:
            pass;
    flag=''
    if(flag=='fail'):
        print('no')
        continue;
    for i in range(centre,n):
        try:
            if(l[i]-l[i+1]!=1):
                flag='fail'
                break;
        except IndexError:
            pass;
    if(flag=='fail'):
        print('no')
        continue;
    print('yes')
