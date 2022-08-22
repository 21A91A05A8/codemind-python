s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s3=''
for i in s1:
    if i in s2:
        if i not in s3:
            if i==' ':
                continue
            s3+=i
print(len(s3))