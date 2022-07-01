n=int(input())
a=list(map(int,input().split()))
min=999
for i in range(0,n):
    if min>a[i]:
        min=a[i]
print(min)        