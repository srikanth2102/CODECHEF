# https://www.codechef.com/ZCOPRAC/problems/ZCO14001
try:
    N,H=map(int,input().split())
    l1=list(map(int,input().split()))
    command=list(map(int,input().split()))
    crane=0
    flag="unpicked"
    for i in command:
        if(i==1 and crane!=0):
            crane=crane-1
        if(i==2 and crane<N-1):
            crane=crane+1
        if(i==3 and flag=="unpicked"):
            if(l1[crane]!=0):
                l1[crane]=l1[crane]-1
                flag="picked"
        if(i==4 and flag=="picked"):
            if(l1[crane]!=H):
                l1[crane]=l1[crane]+1
                flag="unpicked"
        if(i==0):
            break;
    for i in l1:
        print(i,end=" ")
except EOFError:
    pass;
