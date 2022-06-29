import math as mt
 
def isPrime(num):
 
    if (num < 2 or num % 2 == 0):
        return num == 2
    for i in range(3, mt.ceil(mt.sqrt(num + 1))):
        if (num % i == 0):
            return False
    return True
 
def primePalindrome(N):
 
    # if(8<=N<=11) return 11
    #if (8 <= N and N <= 11):
        #return 11
 
    # generate odd length palindrome number
    # which will cover given constraint.
    for x in range(1, 100000):
     
        s = str(x)
        d = s[::-1]
        y = int(s + d[1:])
     
        # if y>=N and it is a prime number
        # then return it.
        if (y >= N and isPrime(y)):
            return y
     
# Driver code
num=int(input())
print(primePalindrome(num))