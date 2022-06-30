n,k=map(int,input().split())
a=list(map(int,input().split()))
count=0
for i in range(0,n):
    if a[i]%k==0:
        count+=1
print(n-count)        