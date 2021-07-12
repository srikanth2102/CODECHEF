#https://www.codechef.com/problems/CFMM
t=int(input())
for i in range(t):
    n=int(input())
    s=''
    for i in range(n):
        temp=str(input())
        s=s+temp
    dic={'c':0,'o':0,'d':0,'e':0,'c':0,'h':0,'e':0,'f':0}
    for i in s:
        if(i=='c'):
            dic['c']+=1
        if(i=='o'):
            dic['o']+=1
        if(i=='d'):
            dic['d']+=1
        if(i=='e'):
            dic['e']+=1
        if(i=='h'):
            dic['h']+=1
        if(i=='f'):
            dic['f']+=1
    dic['c']=dic['c']//2
    dic['e']=dic['e']//2
    print(min(dic.values()))
