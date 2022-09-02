def check(a, n):
    ma = a[1] - a[0]
    for i in range(1, n - 1):
 
        if ((a[i] > a[i - 1] and
             a[i + 1] < a[i]) or
            (a[i] < a[i - 1] and
             a[i + 1] > a[i])):

            ma = max(ma, abs(a[i] - a[i + 1]))
 
        else:
            return False
    return True
if __name__ == '__main__':
   
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    wave = (n - 1) // 2
    if (check(a, n)):
        print(wave)
    else:
        print("-1")