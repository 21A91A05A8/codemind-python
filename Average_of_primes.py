n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in range(0,n):
    r=a[i]
    if(r==1):
        continue
    for j in range(2,int(r**0.5)+1):
        if r%j==0:
            break
    else:
        c+=1
        s+=r
avg=s/c
print('{:.2f}'.format(avg))