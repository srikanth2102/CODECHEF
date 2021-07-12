#https://www.codechef.com/problems/FRGTNLNG
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    reference=map(str,input().split())
    l=[]
    for i in range(k):
        temp=list(map(str,input().split()))
        temp.pop(0)
        l.extend(temp)
    for word in reference:
        if(word in l):
            print("YES",end=' ')
        else:
            print("NO",end=' ')
    print(sep='')

        
        
