class Solution(object):
    def dailyTemperatures(self, T):
        n = len(T)
        res = [0] * n 

        for i in range(n - 2, -1, -1):
            k = i + 1
            while T[i] >= T[k] and res[k] > 0:
                k += res[k]

            if T[k] > T[i]:
                res[i] = k - i

        return res
n=int(input())
T=list(map(int,input().split()))
ob1=Solution()
a=ob1.dailyTemperatures(T)
print(*a)