class Solution:
    def moveZeroes(self, nums):
        for i in range(len(nums)):
            if(nums[i]==0):
                nums.remove(nums[i])
                nums.append(0)
            else:
                continue
ob=Solution()
n=int(input())
nums=list(map(int,input().split()))
ob.moveZeroes(nums)
print(*nums)