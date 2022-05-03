def getSecondMostFreq(str) :
 
    NO_OF_CHARS = 256
 
    # Initialize count list of
    # 256 size with value 0
    count = [0] * NO_OF_CHARS
 
    # count number of occurrences
    # of every character.
    for i in range(len(str)) :
        count[ord(str[i])] += 1
 
    first, second = 0, 0
 
    # Traverse through the count[]
    # and find second highest element.
    for i in range(NO_OF_CHARS) :
 
        # If current element is smaller
        # than first then update both
        # first and second
        if count[i] > count[first] :
 
            second = first
            first = i
        elif (count[i] > count[second] and
            count[i] != count[first] ) :
             
            second = i
 
    # return character
    return chr(second)
 
# Driver code
if __name__ == "__main__" :
 
    str =input()
     
    # function calling
    res = getSecondMostFreq(str)
    if res != NULL :
        print(res)
    else :
        print('-1')    