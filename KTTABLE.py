#https://www.codechef.com/problems/KTTABLE
t=int(input())
for i in range(t):
    n=int(input())
    given=list(map(int,input().split()))
    need=list(map(int,input().split()))
    given.insert(0,0)
    new_given=[]
    for i in range(n):
        try:
            new_given.append(given[i+1]-given[i])
        except IndexError:
            pass;
    count=0
    for i in range(n):
        if(new_given[i]>=need[i]):
            count+=1
    print(count)
