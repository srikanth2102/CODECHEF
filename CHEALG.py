#https://www.codechef.com/problems/CHEALG
t=int(input())
for i in range(t):
    s=str(input())
    current=s[0]
    count=1
    new_s=''
    for i in range(1,len(s)):
        if(s[i]==current):
            count+=1
        if(s[i]!=current):
            new_s=new_s+'a'+str(count)
            current=s[i]
            count=1
    new_s+='a'+str(count)
    if(len(new_s)<len(s)):
        print("YES")
    else:
        print("NO")
