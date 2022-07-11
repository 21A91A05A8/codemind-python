n=int(input())
a=list(map(int,input().split()))
l=[]
c=0
for i in a:
    r=a.count(i)
    if r==1:
        c+=1
        l.append(i)
if c==0:
    print("-1")
else:
    print(max(l))