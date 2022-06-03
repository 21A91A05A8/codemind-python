def seg0s1s(A):
   n = ([i for i in A if i==0] + [i for i in A if i==1])
   print(*n)

if __name__ == "__main__":
   n=int(input())
   A=list(map(int,input().split()))
   seg0s1s(A)