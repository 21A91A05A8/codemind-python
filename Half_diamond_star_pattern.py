def halfDiamondStar(N):
    if N>=3 and N<=100:
        for i in range(N):
            for j in range(0, i + 1):
                 print("*", end = "")
            print()
        for i in range(1, N):
            for j in range(i, N):
                 print("*", end = "")
            print()
    else:
        print("The pattern is not possible")
N=int(input())
halfDiamondStar(N)