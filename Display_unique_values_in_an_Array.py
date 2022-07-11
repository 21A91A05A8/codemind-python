n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    r=a.count(i)
    if r==1:
        c+=1
        print(i,end=' ')
        continue
if c==0:
    print("-1")