class Solution(object):
    def plusOne(self, digits):
         
          num = ""
          for i in digits:
             num +=str(i)
          num = int(num)
          num+=1
          num = str(num)
          ans = []
          for i in num:
             ans.append(int(i))
          return ans
n=int(input())
digits =list(map(int,input().split()))
ob1 = Solution()
a=ob1.plusOne(digits)
print(*a)