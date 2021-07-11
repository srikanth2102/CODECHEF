t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    diff1=c-b
    diff2=b-a
    if(diff1==diff2):
        print(0)
        continue;
    diff=abs(diff1-diff2)
    if(diff%2==0):
        print(diff//2)
    else:
        print(diff//2+1)
