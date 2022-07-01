n=int(input())
arr=list(map(int,input().split()))
res=[]
for i in range(0,len(arr)):
    if arr[i]%2:
        res.append(arr[i])
for i in range(0,len(arr)):
    if arr[i]%2==0:
        res.append(arr[i])
print(*res)