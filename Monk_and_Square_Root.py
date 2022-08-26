import math
t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    c=0
    for i in range(int(math.floor(math.sqrt(m))),n//2+1):
        if((i*i)%n==m):
            print(i)
            c=1
            break
    if c==0:
        print("-1")