s =input()
s = s.lower()
l=[]
d=0
words = s.split() 
vowels = ['a','e','i','o','u'] 
for word in words: 
    c = 0 
    for i in range(0,len(word)): 
        if word[i] in vowels: 
            c+=1 
    l.append(c)
m=min(l)
for i in l:
    if i==m:
        d+=1
print(d)