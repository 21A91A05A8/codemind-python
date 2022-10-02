def create_target_array(nums, index):
    target_list = []
    for num, ind in zip(nums, index):
        target_list.insert(ind, num)
    return target_list
n1=int(input())
nums=list(map(int,input().split()))
n2=int(input())
index=list(map(int,input().split()))
print(*create_target_array(nums, index))