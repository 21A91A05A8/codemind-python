n=int(input())
a=list(map(int,input().split()))
k=int(input())
for i in range(0,n):
    if a[i]==k:
        print('True')
        break
else:
    print('False')