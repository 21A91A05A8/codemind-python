n=int(input())
a=list(map(int,input().split()))
temp=[]
sum=0
for element in a: #elmt there in a
    if(element not in temp):  #not in
        temp.append(element) 
print(*temp)