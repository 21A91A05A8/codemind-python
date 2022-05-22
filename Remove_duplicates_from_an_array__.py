n=int(input())
test_list=list(map(int,input().split()))
res=[]
for i in test_list:
    if i not in res:
        res.append(i)
print(*res)        