s=input()
s=s.lower()
l=''
c=0
for i in s:
    if i not in l:
        if i==' ':
            continue
        l+=i
        c+=1
print(c)