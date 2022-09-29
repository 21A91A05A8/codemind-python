def rearrange(arr,n):
    temp=n*[None]
    small,large=0,n-1
    flag=True
    for i in range(n):
        if flag is True:
            temp[i]=arr[large]
            large-=1
        else:
            temp[i]=arr[small]
            small+=1
        flag=bool(1-flag)
    for i in range(n):
        arr[i]=temp[i]
    return arr
t=int(input())
while(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(*rearrange(arr,n))
    t-=1