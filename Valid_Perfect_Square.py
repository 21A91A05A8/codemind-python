import math
n=int(input())
while(n):
     number = int(input())
     root = math.sqrt(number)
     if int(root + 0.5) ** 2 == number:
         print("True")
     else:
         print("False")
     n-=1     