s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s3=''
for i in s1:
    if i not in s2:
        if i not in s3:
            if i==' ':
                continue
            s3+=i
for i in s2:
    if i not in s1:
        if i not in s3:
            if i==' ':
                continue
            s3+=i
a=sorted(s3)
for i in a:
    print(i,end='')