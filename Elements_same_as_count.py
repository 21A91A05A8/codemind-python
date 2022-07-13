n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    r=l.count(i)
    if i not in a:
        if r==i:
            a.append(r)
if len(a)==0:
    print("-1")
else:
    print(*a)