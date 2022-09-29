class solution(object):
    def maxprofit(self,prices):
        ans=0
        for i in range(1,len(prices)):
            if prices[i]-prices[i-1]>0:
                ans+=(prices[i]-prices[i-1])
        return ans
ob1=solution()
n=int(input())
prices=list(map(int,input().split()))
print(ob1.maxprofit(prices))