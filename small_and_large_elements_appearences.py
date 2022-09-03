s=input()
m=1000
for i in range(0,len(s)):
    r=ord(s[i])
    if s[i]==' ':
        continue
    else:
        if m>r:
            m=r
            m1=s[i]
l=s.count(m1)
n=max(s)
l1=s.count(n)
print(m1,l,n,l1,end=' ')