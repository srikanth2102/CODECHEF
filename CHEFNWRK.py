t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    count=1
    sum=0
    if(max(l)>k):
        print(-1)
        continue;
    for i in range(n):
        sum+=l[i]
        if(sum>k):
            sum=l[i]
            count+=1
        if(sum<=k):
            continue;
    print(count)
