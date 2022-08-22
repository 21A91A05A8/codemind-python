t = int(input())
for j in range(t):
    res=0
    str = input()
    if 'A' not in str or 'B' not in str:
        res = len(str)-1
        print(res)
        continue
    i=0
    while i<(len(str)-1):
        if str[i+1]==str[i]:
            res+=1
        i+=1
    print(res)