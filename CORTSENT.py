# https://www.codechef.com/START4C/problems/CORTSENT
t=int(input())
for i in range(t):
    s1="abcdefghijklm"
    s2="NOPQRSTUVWXYZ"
    l=list(map(str,input().split()))
    l.pop(0)
    for i in l:
        flag=''
        for j in i:
            if(j in s1):
                flag='lower'
            if(flag=='lower' and j in s2):
                flag='fail'
                break;
            if(j in s2):
                flag='upper'
            if(flag=='upper' and j in s1):
                flag='fail'
                break;
            if((j not in s1 )and (j not in s2)):
                flag='fail'
                break;
        if(flag=='fail'):
            flag='break'
            break;
    if(flag=='break'):
        print("NO")
    else:
        print("YES")
