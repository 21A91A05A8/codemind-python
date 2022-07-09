n=int(input())
a=list(map(int,input().split()))
temp=[]
c=0
for element in a:
    if element not in temp:
        temp.append(element) 
    c=0
    for element in temp:
        if element%2:
            c+=1
            continue
print(c)