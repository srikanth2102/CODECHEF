# https://www.codechef.com/MISC2021/problems/MCQ7
try:
    t=int(input())
    for i in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        c=0
        for i in range(n):
            for j in range(i+1,n):
                if(l[i]|l[j]<=max(l[i],l[j])):
                   c=c+1
        print(c)
except EOFError:
    pass;

