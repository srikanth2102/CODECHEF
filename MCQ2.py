# https://www.codechef.com/MISC2021/problems/MCQ2
try:
    def candies(n,l):
        candies=[1]*n
        for i in range(n):
            try:
                if(i==0 and l[0]>l[1]):
                    candies[0]=candies[1]+1
                    continue;
                if(i==0 and l[0]<l[1]):
                    continue;
                if(i==n-1 and l[n-1]<l[n-1-1]):
                    continue;
                if(i==n-1 and l[n-1]>l[n-1-1]):
                    candies[n-1]=candies[n-1-1]+1
                    continue;
                if(l[i]>l[i-1]):
                    candies[i]=candies[i-1]+1
                    continue;
                if(l[i]>l[i+1]):
                    candies[i]=candies[i+1]+1
                    continue;
                if(l[i]<l[i+1] and l[i]<l[i-1]):
                    continue;
            except IndexError:
                pass;
        return(sum(candies))
    n=int(input())
    l=[]
    for i in range(n):
        l.append(int(input()))
    print(candies(n,l))    
except EOFError:
    pass;
