# https://www.codechef.com/LTIME97C/problems/HTMLTAGS
t=int(input())
for i in range(t):
    s=str(input())
    if(len(s)<=3):
        print("Error")
        continue;
    if(" " in s):
        print("Error")
        continue;
    if(s[0]=="<" and s[1]=="/" and s[-1]==">"):
        pass;
    else:
        print("Error")
        continue;
    s=s[2:len(s)-1]
    alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    flag=''
    for i in s:
        if(i not in alp):
            flag='fail'
            break;
    if(flag!='fail'):
        print("Success")
    else:
        print("Error")
