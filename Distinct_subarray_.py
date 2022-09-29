def countoddsum(ar,n):
    result=0
    for i in range(n):
        val=0
        for j in range(i,n):
            val+=ar[j]
            if val%2!=0:
                result+=1
    return result
a=int(input())
b=int(input())
l=[]
for i in range(a,b+1):
    l.append(i)
print(str(countoddsum(l,len(l))))