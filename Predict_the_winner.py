def decideWinner(a, n):
    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(n):
        if (a[i] % 4 == 0):
            count0 += 1
        elif (a[i] % 4 == 1):
            count1 += 1
        elif (a[i] % 4 == 2):
            count2 += 1
        elif (a[i] % 4 == 3):
            count3 += 1
    if (count0 % 2 == 0 and count1 % 2 == 0 and
        count2 % 2 == 0 and count3 == 0):
        return 1
    else:
        return 2
n=int(input())
a =list(map(int,input().split()))
if (decideWinner(a, n) == 1):
    print("X")
else:
    print("Y")