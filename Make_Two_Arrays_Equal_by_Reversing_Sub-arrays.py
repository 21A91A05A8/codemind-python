class Solution:
    def canBeEqual(self, target, arr):
        for i in arr:
            if i in target:
                target.remove(i)
        if len(target)>0:
            return False
        else:
            return True
n=int(input())
target=list(map(int,input().split()))
n1=int(input())
arr=list(map(int,input().split()))
ob1=Solution()
print(ob1.canBeEqual(target, arr))