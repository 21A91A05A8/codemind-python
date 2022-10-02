from collections import Counter
n=int(input())
ini_list = list(map(int,input().split()))
result = [item for items, c in Counter(ini_list).most_common() for item in [items] * c]
a=[]
for i in result:
    if i not in a:
        a.append(i)
print(*a)