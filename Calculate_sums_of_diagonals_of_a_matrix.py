MAX = 100
 
def printDiagonalSums(mat, n):
 
    principal = 0
    secondary = 0;
    for i in range(0, n):
        for j in range(0, n):
 
            # Condition for principal diagonal
            if (i == j):
                principal += mat[i][j]
 
            # Condition for secondary diagonal
            if ((i + j) == (n - 1)):
                secondary += mat[i][j]
         
    print('Principal Diagonal:%d'%principal)
    print('Secondary Diagonal:%d'%secondary)
 
# Driver code
n=int(input())
a = [list(map(int,input().split())) for i in range(n)]
printDiagonalSums(a, n)