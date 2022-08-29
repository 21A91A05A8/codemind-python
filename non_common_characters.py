s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s=''
c=0
for i in s1:
    if i not in s2:
        if i not in s:
            if i==' ':
                continue
            s+=i
            c+=1
for i in s2:
    if i not in s1:
        if i not in s:
            if i==' ':
                continue
            s+=i
            c+=1
lst = [s[i] for i in range(0,len(s))]
lst.sort()
for i in lst:
    print(i, end = "")