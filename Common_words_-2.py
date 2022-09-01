s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
w1=s1.split()
w2=s2.split()
s3=''
c=0
for i in w1:
    if i in w2:
        if i not in s3:
            if s1.count(i)==1:
                if s2.count(i)==1:
                    if i==' ':
                        continue
                    s3+=i+' '
                    c+=1
print(c)