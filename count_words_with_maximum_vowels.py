s =input()
s = s.lower()
l=[]
count=0
words = s.split() 
vowels = ['a','e','i','o','u'] 
for word in words: 
    c = 0 
    for i in range(0,len(word)): 
        if word[i] in vowels: 
            c+=1 
    l.append(c)
b=max(l)
for j in l:
    if j==b:
        count+=1
print(count)