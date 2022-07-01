n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=[]
for i in a:
    if (i not in b) and (i not in res):
        res.append(i)
for i in b:
    if (i not in a) and (i not in res):
        res.append(i)
print(len(res))        