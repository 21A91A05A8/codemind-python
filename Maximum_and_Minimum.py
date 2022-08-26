n=int(input())
a=list(map(int,input().split()))
c=-1
b=[]
for i in a:
    if a.count(i)==i:
        b.append(i)
        c+=1
if c!=-1:
    print(min(b),max(b),end=' ')
else:
    print("-1")