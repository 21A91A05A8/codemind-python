class Solution:
   def solve(self, s0, s1):
      s0 = s0.lower()
      s1 = s1.lower()
      s0List = s0.split(" ")
      s1List = s1.split(" ")
      return len(list(set(s0List)&set(s1List)))
ob = Solution()
S = input()
T = input()
print(ob.solve(S,T))