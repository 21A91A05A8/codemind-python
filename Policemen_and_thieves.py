def solution (A, K):
    count = 0
    for i in range(len(A)):
        ex=0
        while "P" in A[i]:
            Pj = A[i].index("P")
            if "T" in A[i]:
                Tj = A[i].index("T")
                dist = abs(Tj-Pj)
                ex = min(Tj,Pj)
                if dist<=K:
                    count+=1
                    A[i][Pj] = "X"
                    A[i][Tj] = "X"
                    A[i] = A[i][ex+1:]
                else:
                    A[i][ex] = "X"
            else:
                break
    return count
    
t=int(input())
while(t):
    n,K=map(int,input().split())
    A=[list(map(str,input().split())) for i in range(n)]
    print(solution(A,K))