n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=[]
for element in a:
    if(element not in b and element not in res):
        res.append(element)
for element in b:
    if(element not in a and element not in res):
        res.append(element)        
print(*res)