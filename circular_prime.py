def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
d=0
if prime(n):
    k=n
    rev=0
    while n:
     r=n%10
     n=n//10
     rev=rev*10+r
     if prime(rev):
         d=1
     else:
         d=2
if d==1:
    print('circular prime')
elif d==2:
    print('prime but not a circular prime')
else:
    print('not prime')