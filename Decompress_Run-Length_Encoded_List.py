class Solution:
    def decompressRLElist(self, nums):
        decompressed = []
        
        for i in range(0, len(nums)-1, 2):
            decompressed = decompressed + nums[i] * [nums[i+1]]
    
        return decompressed
ob=Solution()
n=int(input())
nums=list(map(int,input().split()))
print(*(ob.decompressRLElist(nums)))