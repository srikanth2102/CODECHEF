#https://www.codechef.com/problems/QUALPREL
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort(reverse=1)
    count=0
    for i in l:
        if(i>=l[k-1]):
            count+=1
    print(count)
