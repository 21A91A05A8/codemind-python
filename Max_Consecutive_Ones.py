class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
                        
        return max(max_count, count)
n=int(input())
nums=list(map(int,input().split()))
ob1 = Solution()
a=ob1.findMaxConsecutiveOnes(nums)
print(a)