n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(0,n-1,2):
    r=a[i]
    s=a[i+1]
    for j in range(0,s):
        l.append(r)
print(*l)