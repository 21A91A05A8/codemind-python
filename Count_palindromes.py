def palindrome(b):
    k=b
    rev=0
    while(b):
        d=b%10
        rev=(rev*10)+d
        b=b//10
    if(rev==k):
        return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
count=0
for i in range(0,n):
    if palindrome(a[i]):
        count+=1
print(count)        