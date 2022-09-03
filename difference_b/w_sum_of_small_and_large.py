s=input()
s=s.split()
s1=0
s2=0
for word in s:
    for i in word:
        m=min(word)
        n=max(word)
    s2+=ord(m)
    s1+=ord(n)
print(s1-s2)