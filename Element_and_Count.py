n=int(input())
a=list(map(int,input().split()))
l=[]
r=[]
for i in a:
    if i not in l:
        l.append(i)
for i in range(0,len(l)):
    c=a.count(l[i])
    r.append(l[i])
    r.append(c)
print(*r)