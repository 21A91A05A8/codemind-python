n=int(input())
max=0
while(n>0):
    d=n%10
    n=n//10
    if(d>max):
        max=d
print(max)