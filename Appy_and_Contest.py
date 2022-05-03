def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
for jj in range(int(input())):
    n,a,b,k=map(int,input().split())
    na,nb=n//a,n//b
    nc=n//((a*b)//gcd(min(a,b),max(a,b)))
    
    if na+nb-2*nc>=k:
        print('Win')
    else:
        print('Lose')