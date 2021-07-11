t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    count=0
    sum1=sum(l)
    for i in range(n):
        temp=l[i]+k
        if(temp>sum1-l[i]):
            count+=1
    print(count)
