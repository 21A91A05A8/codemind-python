class Solution(object):
    def balancedStringSplit(self, s):
        result, count = 0, 0      
        for c in s:
            count += 1 if c == 'L' else -1            
            if count == 0:
                result += 1
        return result
s=input()
ob1=Solution()
print(ob1.balancedStringSplit(s))