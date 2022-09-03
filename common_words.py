s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s1=s1.split()
s2=s2.split()
for word1 in s2:
    if word1 in s1:
        print(word1,end=' ')