class Solution(object):
    def searchRange(self,nums,target):
        res=[-1,-1]
        low=0
        high=len(nums)
        while low<high:
            mid=int(low+(high-low)//2)
            if nums[mid]==target:
                high=mid
                res[0]=mid
                res[1]=mid
            elif nums[mid]<target:
                 low=mid+1
            else:
                 high=mid
        if res[0]==-1:
            return res
        low=res[0]+1
        high=len(nums)
        while low<high:
            mid=int(low+(high-low)//2)
            if nums[mid]==target:
                low=mid+1
                res[1]=mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid
        return res
n=int(input())
nums=list(map(int,input().split()))
target=int(input())
ob1=Solution()
a=ob1.searchRange(nums,target)
print(*a)