#https://www.codechef.com/problems/CHCUBE
t=int(input())
for i in range(t):
    l=list(map(str,input().split()))
    c,count=0,0
    if(l[0] in l[2:4]):
        count+=1
    if(l[0] in l[4:]):
        count+=1
    if(l[1] in l[2:4]):
        c+=1
    if(l[1] in l[4:]):
        c+=1
    if(c==2 or count==2):
        print("YES")
    else:
        print("NO")
