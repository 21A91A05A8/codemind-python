n=int(input())
l=[]
for i in range(n):
    w=int(input())
    l.append(w)
t=int(int(input()))
c=0
for i in range(len(l)):
    if (l[i]<=t):
        c+=1
    if(l[i]>t):
        c+=2
print(c)