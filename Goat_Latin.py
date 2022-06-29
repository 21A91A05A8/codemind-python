class Solution:
   def toGoatLatin(self, S):
      temp = S.split(" ")
      counter = 1
      result = []
      vowel = {"a","e","i","o","u"}
      for i in temp:
         if i[0].lower() in vowel:
            x = i + "ma" + ("a"*counter)
         else:
            x=i[1:]+i[0] + "ma" +("a"*counter)
         counter+=1
         result.append(x)
      return " ".join(c for c in result)
ob1 = Solution()
print(ob1.toGoatLatin(input()))