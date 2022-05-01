sum=0  
# Ask user to enter the number  
num=int(input())  
# temporary variable  store copy of the original number  
temp=num  
# Using while loop  
while(num):  
    # intialize with 1  
    i=1  
    # fact variable with 1  
    fact=1  
    rem=num%10  
    while(i<=rem):  
        fact=fact*i   # Find factorial of each number  
        i=i+1  
    sum=sum+fact  
    num=num//10  
if(sum==temp):  
    print("The number",temp,"is a strong number")  
else:  
    print("The number",temp, "is not a strong number")  