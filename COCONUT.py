#https://www.codechef.com/JUNE21C/problems/COCONUT
try:
    t=int(input())
    for i in range(t):
        xa,xb,XA,XB=map(int,input().split())
        a=XA//xa
        if(XA%xa!=0):
            a+=1
        b=XB//xb
        if(XB%xb!=0):
            b+=1
        print(a+b)
except EOFError:
    pass;
