s=input()
s=s.split()
for word in s:
    for i in word:
        m=min(word)
        n=max(word)
    print(abs(ord(m)-ord(n)),end=' ')