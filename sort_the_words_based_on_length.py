mylist=input().split()
mylist.sort()
mylist = sorted(mylist, key=len, reverse=False)
str1 = ""
# traverse in the string 
l = ' '.join([str(elem) for elem in mylist])
print(l)