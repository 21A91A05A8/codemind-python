s=input()
s=s.lower()
l=''
v=''
c=0
for i in s:
    if i not in l:
        if i==' ':
            continue
        l+=i
        c+=1
r=sorted(l)
for i in r:
    if i==' ':
        continue
    else:
        v+=i
print(v)