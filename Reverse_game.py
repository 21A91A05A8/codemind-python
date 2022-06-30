n=int(input())
a=list(map(int,input().split()))
rev=0
l=[]
for i in range(0,n):
    k=a[i]
    while k>0:
        d=k%10
        rev=rev*10+d
        k=k//10
    l.append(rev)
    rev=0
print(*l)    