n=int(input())  
c=1
a = list(map(int,input().split())) #list
for i in range(0,n):
    c=1
    if a[i]>0:
        for j in range(i+1,n):
            if a[i]==a[j]:
                c+=1
                a[j]=-1  
        print(a[i],c,end=' ')