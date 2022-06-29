from math import sqrt
 
# Function to factors of the given
# number
def getFactorization(x):
     
    count = 0
    v = []
 
    # Loop to find the divisors of
    # the number 2
    while (x % 2 == 0):
        count += 1
        x = x // 2
 
    if (count != 0):
        v.append(count)
 
    # Loop to find the divisors of the
    # given number upto SQRT(N)
    for i in range(3, int(sqrt(x)) + 12):
        count = 0
         
        while (x % i == 0):
            count += 1
            x //= i
             
        if (count != 0):
            v.append(count)
 
    # Condition to check if the rest
    # number is also a prime number
    if (x > 1):
        v.append(1)
         
    return v
 
# Function to find the non-prime
# divisors of the given number
def nonPrimeDivisors(N):
     
    v = getFactorization(N)
    ret = 1
 
    # Loop to count the number of
    # the total divisors of given number
    for i in range(len(v)):
        ret = ret * (v[i] + 1)
    ret = ret - len(v)
     
    return ret
 
# Driver Code
if __name__ == '__main__':
     
    N = int(input())
 
    # Function Call
    print(nonPrimeDivisors(N))