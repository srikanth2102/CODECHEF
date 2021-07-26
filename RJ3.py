# https://www.codechef.com/CDIG2021/problems/RJ3
from itertools import combinations
t=int(input())
for i in range(t):
    n=int(input())
    l=[1]
    flag=''
    i=1
    while(i<n):
        i=i*2
        l.append(i)
    for i in range(2,len(l)+1):
        perm=list(combinations(l,i))
        for j in perm:
            if(sum(j)==n):
                print(i)
                flag="pass"
                break;
        if(flag=="pass"):
            break;
