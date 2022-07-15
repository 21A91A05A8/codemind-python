string=input()
vowels=0
l=''
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
          vowels+=1
          if i not in l:
              l+=i
if vowels==0:
    print("-1")
else:
    for j in l:
        print(j,end=' ')
              
         