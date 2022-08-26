n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=[]
c=-1
for i in a:
    if a.count(i)==k:
        if i not in b:
            b.append(i)
        c+=1
if c!=-1:
    print(*b)
else:
    print("-1")