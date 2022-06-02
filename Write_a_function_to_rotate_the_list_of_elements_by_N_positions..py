x=int(input())
list_1 =list(map(int,input().split()))
n=int(input())
if n>len(list_1):
    n = int(n%len(list_1))
list_1 = (list_1[-n:] + list_1[:-n])
a=list_1
print(*a)