class Solution:
    def diStringMatch(self, S):
        A=[i for i in range(len(S)+1)]
        return [A.pop((j=='I')-1) for j in S]+A
ob = Solution()
print(*ob.diStringMatch(input("")))