#https://www.codechef.com/ZCOPRAC/problems/ZCO14003
try:
    N=int(input())
    l1=[]
    for i in range(N):
        l1.append(int(input()))  
    l1.sort()
    l2=[]
    for i in range(N):
        revenue=l1[i]*(N-i)
        l2.append(revenue)
    print(max(l2))    
except EOFError:
    pass;
