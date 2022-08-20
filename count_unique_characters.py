s=input()
s=s.lower()
s1=''
for i in s:
    if s.count(i)==1:
        if i not in s1:
            if i==' ':
                continue
            s1+=i
print(len(s1))