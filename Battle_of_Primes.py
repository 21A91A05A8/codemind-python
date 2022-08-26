def isprime(r):
    for i in range(2,r):
        if (r%i) == 0:
            return 0
    else:
        return 1
n1=int(input())
n2=int(input())
n=n1+n2
a=[]
for i in range(1,100):
    k=n+i
    if(isprime(k)):
        print(i)
        break