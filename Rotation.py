testCase = int(input())
i = 0
while i < testCase:
      n, rotation = input().split()
      nums = list(map(int,input().split()))
      rotation = int(rotation) % int(n) 
      print(" ".join(str(x) for x in nums[-int(rotation):] + nums[:-int(rotation)]))
      i+=1