#https://www.codechef.com/problems/HORSES
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    diff=[]
    for i in range(n):
        try:
            diff.append(l[i+1]-l[i])
        except IndexError:
            pass;
    print(min(diff))
