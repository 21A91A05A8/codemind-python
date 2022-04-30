num=int(input())
if((num!=0)or(num!=1)):
    a=0
    b=1
    c=a+b
    while (c<num):
        a=b
        b=c
        c=a+b
    if c==num:
        print("True")
    else:
        print("False")