n=int(input())
count=0
for i in range (1,n):
    if(i*(i+1)==n):
        count=0
        break
    else:
        count=1
if count==0:
    print("YES")
else:
    print("NO")