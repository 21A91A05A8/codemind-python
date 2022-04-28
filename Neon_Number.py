num = int(input())
sqr = num*num 
s= 0
while sqr>0:
    s=s + sqr%10
    sqr = sqr//10
if (num == s):
    print("Neon Number")
else:
    print("Not Neon Number")