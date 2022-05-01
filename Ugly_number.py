n=int(input())
flag=0
while n!=1:
    if n%2==0:
        n=n//2
    elif n%3==0:
        n=n//3
    elif n%5==0:
        n=n//5
    else:
        print("Not Ugly Number")
        flag=1
        break
if flag==0:
    print("Ugly Number")