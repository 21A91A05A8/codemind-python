a=int(input())#perivious prime
for n in range(a,1,-1):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            break
    else:
        #print(n)
        break
b=a
while True:
       for i in range(2,int(a**0.5)+1):#next prime
          if a%i==0:
            break
       else:
          #print(a)
          break
       a+=1
if abs(b-n)>=abs(a-b):
    print(abs(a-b))
else:
    print(abs(b-n))