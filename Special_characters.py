def solve(string):
    even=[]
    odd=[]
    special_char=0
    for ch in string:
        if(ch.isalnum() == False):
            special_char+=1
        elif(ch.isdigit()):
            if int(ch)%2==0:
                even.append(ch)
            else:
                odd.append(ch)
                 
    if(special_char%2!=0):
          odd, even=even, odd             
    even_len=len(even)
    odd_len=len(odd)
    m=max(even_len, odd_len)
    ev=0
    ox=0
    for i in range(m):
        if(ev!=even_len):
            print(even[ev], end='')
            ev+=1
        if(ox!=odd_len):
            print(odd[ox], end='')
            ox+=1
    print()
 
 # Driver code   
s=input()
solve(s)