#https://www.codechef.com/problems/CO92JUDG
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.remove(max(a))
    b.remove(max(b))
    if(sum(a)>sum(b)):
        print('Bob')
        continue;
    if(sum(a)==sum(b)):
        print("Draw")
        continue
    else:
        print("Alice")
