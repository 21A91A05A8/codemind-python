class Solution(object):
    def maximum69Number (self, num):
        curr, base, change = num, 3, 0
        while curr:
            if curr%10 == 6:
                change = base
            base *= 10
            curr //= 10
        return num+change
num=int(input())
ob1=Solution()
a=ob1.maximum69Number (num)
print(a)