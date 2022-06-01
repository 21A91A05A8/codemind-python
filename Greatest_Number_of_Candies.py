class solution:
    def kidswithcandies(self,candies,extracandies):
        l=len(candies)
        ans=[]
        for i in range(l):
            if candies[i]+extracandies>=max(candies):
                ans.append(True)
            else:
                ans.append(False)
        return ans
n=int(input())
candies=list(map(int,input().split()))
extracandies=int(input())
ob1=solution()
a=ob1.kidswithcandies(candies,extracandies)
print(*a)