n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(0,n):
    r=a[i]
    while(r):
        d=r%10
        s+=d
        r=r//10
print(s)