#https://www.codechef.com/LTIME95B/problems/BENCHP
t=int(input())
for i in range(t):
    n,w,rod=map(int,input().split())
    l=list(map(int,input().split()))
    if(rod>=w):
        print('YES')
        continue;
    dic={}
    for i in l:
        if(i in dic):
            dic[i]+=1
        else:
            dic[i]=1
    sum=0
    for i in dic.keys():
        if(dic[i]%2==0):
            sum+=i*dic[i]
    if(sum+rod>=w):
        print('YES')
        continue;
    print('NO')
