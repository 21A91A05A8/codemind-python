n=int(input())
k=n
i=k*k
rev=0
jrev=0
while (n!=0):
    d=n%10
    rev=(rev*10)+d
    n=n//10
j=rev*rev 
while (j!=0):
    e=j%10
    jrev=(jrev*10)+e
    j=j//10
if jrev==i:
    print("True")
else:
    print("False")