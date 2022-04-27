num = int(input())

# If number is greater than 1
if num > 1:
   # Check if factor exist  
   for i in range(2,num):
       if (num % i) == 0:
           print("not a prime")
           break
   else:
       print("prime")
       
# Else if the input number is less than or equal to 1
else:
   print("not a prime")