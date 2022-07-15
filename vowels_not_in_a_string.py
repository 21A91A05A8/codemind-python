s=input()
s=s.lower()
c=0
if s.count('a')==0:
    c+=1
    print('a',end=' ')
if s.count('e')==0:
    c+=1
    print('e',end=' ')
if s.count('i')==0:
    c+=1
    print('i',end=' ')
if s.count('o')==0:
    c+=1
    print('o',end=' ')
if s.count('u')==0:
    c+=1
    print('u',end=' ')
if c==0:
    print("0")