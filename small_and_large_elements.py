s=input()
s=s.split()
for i in range(0,len(s)):
    if i==0:
        m=min(s[i])
        print(m,end=' ')
    if i==len(s)-1:
        n=max(s[i])
        print(n,end='')