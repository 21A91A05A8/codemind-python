n=int(input())
a=list(map(int,input().split()))
temp=[]
c=0
for element in a: #elmt there in a
    if(element not in temp):  #not in
        temp.append(element) 
    c=0
    for element in temp:
        if element%2==0:
            c+=1
            continue
print(c)