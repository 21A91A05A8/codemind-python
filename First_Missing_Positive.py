class Solution:
    def firstMissingPositive(self, A):
        i = 0
        while i < len(A):
            if A[i] > 0 and A[i] - 1 < len(A) and A[i] != A[A[i]-1]:
                A[A[i]-1], A[i] = A[i], A[A[i]-1]
            else:
                i += 1
        
        for i, integer in enumerate(A):
            if integer != i + 1:
                return i + 1
        return len(A) + 1
    
if __name__ == "__main__":
    n=int(input())
    A=list(map(int,input().split()))
    ob1=Solution()
    print(ob1.firstMissingPositive(A))