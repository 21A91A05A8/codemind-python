from collections import Counter

def sockMerchant(n,arr):
    n = Counter(arr)
    return sum(i//2 for i in n.values())

n = input()
arr = list(map(int,input().split()))
print(sockMerchant(n,arr))  