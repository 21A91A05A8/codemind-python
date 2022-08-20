s=input()
s=s.lower()
s1=''
for i in s:
    if i not in s1:
        if i==' ':
            continue
        s1+=i
r=sorted(s1)
for i in r:
    print(i,end='')