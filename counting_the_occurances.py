def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

lst = input()
x = input()
if countX(lst, x) != 0:
    print(countX(lst, x))
else:
    print(-1)