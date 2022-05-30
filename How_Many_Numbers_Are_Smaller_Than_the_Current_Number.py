class solution:
    def smallerNumbersThanCurrent(self,nums):
        l=len(nums)
        ans=[]
        count=0
        for i in nums:
            for j in range(l):
                if(nums[j]-i)<0:
                    count+=1
            ans.append(count)
            count=0
        return ans
n=int(input())
nums=list(map(int,input().split()))
ob1=solution()
a=ob1.smallerNumbersThanCurrent(nums)
print(*a)