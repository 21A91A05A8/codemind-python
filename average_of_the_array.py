n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(0,n):
    s=s+a[i]
avg=s/n
print("{:.2f}".format(avg))