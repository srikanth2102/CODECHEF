# https://www.codechef.com/problems/GOODLS1
t=int(input())
for i in range(t):
    s=str(input())
    dic={}
    for i in s:
        if(i in dic):
            dic[i]+=1
        else:
            dic[i]=1
    count=0
    for i in dic.values():
        if(i>1):
            count+=i-1
    print(count)
