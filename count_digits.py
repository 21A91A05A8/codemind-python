n=int(input())
a=list(map(int,input().split()))
for k in a:
    k=abs(k)
    k=str(k)
    print(len(k),end=' ')