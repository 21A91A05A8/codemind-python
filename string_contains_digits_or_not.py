t=int(input())
while t>0:
     string = str(input())
     digit=letter=0
     for ch in string:
         if ch.isdigit():
            digit=digit+1
     if (digit!=0):
         print("Yes" )
     else:
         print("No")
     t-=1         