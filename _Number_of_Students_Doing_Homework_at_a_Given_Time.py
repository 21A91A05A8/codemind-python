class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        return sum([True for i,j in zip(startTime,endTime) if i<=queryTime<=j])
ob=Solution()
n1=int(input())
l1=list(map(int,input().split()))
n2=int(input())
l2=list(map(int,input().split()))
t=int(input())
print(ob.busyStudent(l1,l2,t))