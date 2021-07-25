#https://www.codechef.com/problems/PPATTERN
t=int(input())
for i in range(t):
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append([0]*n)
arr[0][0]=1
arr[n-1][n-1]=n**2
temp=0
for i in range(n):
    for j in range(n):
        if(i==0 and arr[i][j]==0):
            arr[i][j]=temp+j+1
            temp=arr[i][j]
print(arr)
