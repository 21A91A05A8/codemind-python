n=int(input())
sum=0
p=1
while(n>0):
    rem=n%10
    sum+=rem
    p=p*rem
    n=n//10
if(sum==p):
    print("Spy Number")
else:
    print("Not Spy Number")