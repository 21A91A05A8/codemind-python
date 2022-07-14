n=int(input())
l=list(map(int,input().split()))
if n%2:
    l.append(0)
print(*l)