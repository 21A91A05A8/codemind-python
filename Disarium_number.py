import math
n=int(input())
k=n
r=k
dc=0
c=0
sum=0
while n>0:
    d=n%10
    n=n//10
    dc+=1
while k>0:
    e=k%10
    k=k//10
    sum+=math.pow(e,dc)
    dc-=1
if sum==r:
    print("True")
else:
    print("False")