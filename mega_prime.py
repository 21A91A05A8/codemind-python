n=int(input())
a=n
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print('Not Mega Prime')
        break
else:
    d=0
    pd=0
    while n:
        rem=n%10
        n=n//10
        d+=1
        if rem==2 or rem==3 or rem==5 or rem==7:
            pd+=1
if d==pd:
    print('Mega Prime')
else:
    print('Not Mega Prime')