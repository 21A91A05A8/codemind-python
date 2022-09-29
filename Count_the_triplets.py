def count_Triplets(A, N):
    count = 0
    A.sort()
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if A[i] + A[j] == A[k]:
                    count = count + 1
    if(count==0):
        return "-1"
 
    return count
 
t=int(input())
while(t):
    n=int(input())
    l=list(map(int,input().split()))
    print(count_Triplets(l,n))
    t-=1