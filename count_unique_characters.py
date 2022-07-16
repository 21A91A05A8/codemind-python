s=input()
s=s.lower()
v=''
c=0
for i in s:
    if s.count(i)==1:
        v+=i
r=sorted(v)
for i in r:
    if i==' ':
        continue
    else:
        c+=1
print(c)