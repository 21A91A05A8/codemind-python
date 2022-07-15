s =input()
s = s.lower()
words = s.split() 
vowels = ['a','e','i','o','u'] 
for word in words: 
    c = 0 
    for i in range(0,len(word)): 
        if word[i] in vowels: 
            c+=1 
    print(c,end=' ')