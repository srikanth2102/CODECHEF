# https://www.codechef.com/START4C/problems/QUIZPLAG
t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    l=list(map(int,input().split()))
    dic={}
    for i in l:
        if(i in dic):
            dic[i]=dic[i]+1
        else:
            dic[i]=1
    l1=[]
    for i in range(1,n+1):
        if(i in dic):
            if(dic[i]>1):
                l1.extend([i]*dic[i])
    if(l1==[]):
        print(0)
        continue;
    else:
        l1=set(l1)
        l1=list(l1)
        l1.sort()
        print(len(l1),end=' ')
        for i in l1:
            print(i,end=' ')
        print(sep=' ')
