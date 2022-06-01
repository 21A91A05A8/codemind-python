class Solution(object):
    def search(self, nums, target):
        
        if len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        while (left <= right):
            
            mid = left + (right - left)//2
            
            if nums[mid] == target:
                return mid
            
            #check if left side is sorted
            if (nums[left] <= nums[mid]):
                if (target >= nums[left] and target < nums[mid]):
                    right = mid - 1
                else:
                    left = mid + 1
                    
            #right hand side is sorted
            else:
                if (target > nums[mid] and target <= nums[right]):
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1
n=int(input())
nums =list(map(int,input().split()))
target=int(input())
ob1 = Solution()
a=ob1.search(nums,target)
print(a)