# https://www.codechef.com/LTIME97C/problems/FALSNUM
t=int(input())
for i in range(t):
    s=str(input())
    if(s[0]!='1'):
        s='1'+s
    else:
        s=s[0]+'0'+s[1:]s
    print(s)
