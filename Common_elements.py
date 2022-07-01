n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=[]
for element in a:
    if(element in b and element not in res):
        res.append(element)
print(*res)