class Solution(object):
    def maxSubarraySumCircular(self, A):
        total, max_sum, cur_max, min_sum, cur_min = 0, -float("inf"), 0, float("inf"), 0
        for a in A:
            cur_max = max(cur_max+a, a)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min+a, a)
            min_sum = min(min_sum, cur_min)
            total += a
        return max(max_sum, total-min_sum) if max_sum >= 0 else max_sum
ob=Solution()  
n=int(input())
A=list(map(int,input().split()))
print(ob.maxSubarraySumCircular(A))