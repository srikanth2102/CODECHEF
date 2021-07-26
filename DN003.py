# https://www.codechef.com/NERD2021/problems/DN003
try:
    def change(l,i,n):
        for i in range(i+1,n):
            if(l[i]==0):
                l[i]=1
                continue;
            if(l[i]==1):
                l[i]=0
                continue;
        return(l)        
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    for i in range(n):
        if(l[i]==1):
            continue;
        if(l[i]==0):
            s=s+1
            l=change(l,i,n)
    print(s)        
except EOFError:
    pass;

        
        
