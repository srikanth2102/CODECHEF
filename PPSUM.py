#https://www.codechef.com/problems/PPSUM
t=int(input())
for i in range(t):
    d,n=map(int,input().split())
    n1=n
    for i in range(d):
        sum=0
        for j in range(1,n1+1):
            sum=sum+j
        n1=sum
    print(sum)
