from collections import defaultdict
def countSubarrayswithSumK(a, K):
    n = len(a)
    hash = defaultdict(lambda: 0)
    count = 0
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum == K:
            count += 1
        if (sum - K) in hash:
            count += hash[sum - K]
        hash[sum] += 1
    return count
n,K=map(int,input().split())
a=list(map(int,input().split()))
print(countSubarrayswithSumK(a, K))