n=int(input())
a=list(map(int,input().split()))
l=[]
c=0
for i in a:
    if i not in l:
        l.append(i)
for j in range(0,len(l)):
    r=a.count(l[j])
    if r==l[j]:
        c+=1
print(c)