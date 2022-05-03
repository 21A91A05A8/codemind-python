t = int(input())
for i in range(t):
    l,r = map(int,input().split())
    d=[]
    for i in range(l,r+1):
        a =str(i)
        if a.endswith('2') or a.endswith('3') or a.endswith('9'):
            d.append(a)
    print(len(d))