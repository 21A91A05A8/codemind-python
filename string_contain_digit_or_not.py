string=str(input())
digit =letters=0
for ch in string:
    if ch.isdigit():
        digit=digit+1
if (digit!=0):
        print("Contains",digit,"digit")
else:
        print("Doesn't contain digit")