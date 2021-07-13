#https://www.codechef.com/problems/RAINBOWA
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    ref=(1,2,3,4,5,6,7)
    flag=''
    for i in l:
        if(i not in ref):
            print("no")
            flag='fail1'
            break;
    if(flag=='fail1'):
        continue;
    for i in ref:
        if(i not in l):
            print("no")
            flag='fail2'
            break;
    if(flag=='fail2'):
        continue;
    if(n%2==0):
        length=n//2
    else:
        length=n//2+1
    temp=l[0:length]
    temp.sort()
    temp=temp[::-1]
    if(n%2==0):
        if(temp==l[length:]):
            print("yes")
        else:
            print("no")
    if(n%2!=0):
        if(temp==l[length-1:]):
            print("yes")
        else:
            print("no")
