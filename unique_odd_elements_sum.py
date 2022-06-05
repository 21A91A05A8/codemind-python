n=int(input())
a=list(map(int,input().split()))
temp=[]
sum=0
for element in a: #elmt there in a
    if(element not in temp):  #not in
        temp.append(element) 
    sum=0
    for element in temp:
        if element%2!=0:
            sum+=element
            continue
print(sum)