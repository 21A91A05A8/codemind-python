class solution(object):
    def findNumbers(self,nums):
        str_num=map(str,nums)
        count=0
        for s in str_num:
            if len(s)%2==0:
                count+=1
        return count
n=int(input())
nums=list(map(int,input().split()))
ob1=solution()
a=ob1.findNumbers(nums)
print(a)