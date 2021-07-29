# https://www.codechef.com/problems/CHGM1
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    temp=-100000000000000
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=l[j]
            if(sum>temp):
                temp=sum
    print(temp)
            
