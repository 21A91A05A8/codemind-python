n=int(input())
c=0
for i in range(1,n//2):
    for j in range(1,n//2):
        if (i**2)*(j**2)==n:
            c=1
            break
if c==1:
    print('True')
else:
    print('False')