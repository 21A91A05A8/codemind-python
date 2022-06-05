n=int(input())  #5
a = list(map(int,input().split())) #list: 2 33 4 33 5
temp = []
sum=0
for element in a: 
    if(element not in temp):  
        temp.append(element) #uniq elmts stored
        if element in temp:
            sum+=element
            continue
print(sum)