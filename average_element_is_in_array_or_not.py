n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(0,n):
    s=s+a[i]
avg=s//n
for i in range(0,n):
    if a[i]==avg:
        print('True')
        break
else:
    print('False')