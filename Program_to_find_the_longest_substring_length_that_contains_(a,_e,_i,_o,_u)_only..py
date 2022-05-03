# Python3 program to find the
# longest substring of vowels.
def isVowel(c):
    return (c == 'a' or c == 'e' or
            c == 'i' or c == 'o' or
            c == 'u')          
 
def longestVowel(s):
    count, res = 0, 0
     
    for i in range(len(s)):
 
        # Increment current count
        # if s[i] is vowel
        if (isVowel(s[i])):
            count += 1 
 
        else:
        
            # check previous value
            # is greater then or not
            res = max(res, count)
            count = 0
    return max(res, count)
 
# Driver code
if __name__ == "__main__":
    s = input()
    print (longestVowel(s))
    