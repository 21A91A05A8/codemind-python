def isPalindrome(n):
    for i in range(len(n) // 2):
        if (n[i] != n[-1 - i]):
            return False
 
    return True
 
# Convert number into String
 
 
def convertNumIntoString(num):
 
    Snum = str(num)
    return Snum
 
# Function return closest Palindrome number
 
 
def closestPalindrome(num):
 
    # Case1 : largest palindrome number
    # which is smaller than given number
    RPNum = num - 1
    while (not isPalindrome(
           convertNumIntoString(abs(RPNum)))):
        RPNum -= 1
    SPNum = num + 1
    while (not isPalindrome(
           convertNumIntoString(SPNum))):
        SPNum += 1
 
    # Check absolute difference
    if (abs(num - RPNum) > abs(num - SPNum)):
        print (SPNum)
    elif (abs(num - RPNum) == abs(num - SPNum)):
        print(RPNum,SPNum,end=' ')
    else:
        print(RPNum)
 
 
# Driver Code
if __name__ == '__main__':
 
    num =int(input())
    closestPalindrome(num)