#https://www.codechef.com/problems/EVENM
t=int(input())
for i in range(t):
    n=int(input())
    for i in range(n):
        temp=i*n
        if(i%2==0):
            for k in range(1,n+1):
                print(k+temp,end=' ')
        if(i%2!=0):
            for k in range(n,0,-1):
                print(k+temp,end=' ')
        print(sep='')
            
                
