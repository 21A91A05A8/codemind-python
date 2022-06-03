n=int(input())
a=list(map(int,input().split()))
sum1=0
sum2=0
for i in range(0,n):
    if(i%2):
        sum1+=a[i]
    else:
        sum2+=a[i]
diff=sum1-sum2
if diff==0:
    print('YES')
else:
    print('NO')