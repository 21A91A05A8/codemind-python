n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
count=0
for i in range(0,n):
    if a[i]==0:
        if(k==1):
            count+=1
    if a[i]<0:
        a[i]=abs(a[i])
    r=a[i]
    while(r>0):
        d=r%10
        c+=1
        r=r//10
    if(k==c):
        count+=1
        c=0
    else:
        c=0
print(count)