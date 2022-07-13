n,m=map(int,input().split())
test_list = [list(map(int,input().split())) for i in range(n)]
  
# using max() + list comprehension + zip()
# Maximum of each Column
res=[max(idx) for idx in zip(*test_list)]
# print result
for i in range(0,len(res)):
    print(res[i])