class Solution:
    def canConstruct(self,ransomNote,magazine):
        magazine = list(magazine)
        for i in ransomNote:
            if i in magazine:
                magazine.remove(i)
            else:
                return False
        return True
a=Solution()
ransomNote,magazine=map(str,input().split())

print(a.canConstruct(ransomNote,magazine))