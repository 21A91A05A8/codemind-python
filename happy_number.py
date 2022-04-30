num=int(input())
sum=0
while sum!=1 and sum!=4:
    sum=0
    while num>0:
       j=num%10
       sum+=j*j
       num=num//10
    num=sum
if sum==1:
    print("True")
else:
    print("False")