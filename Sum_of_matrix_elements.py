n=int(input())
m=int(input())
a=[list(map(int,input().split())) for i in range(n)]
s=0
for i in range(n):
    for j in range(m):
        s+=a[i][j]
print(s)