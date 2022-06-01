def maxRepeating(str):
 
    l = len(str)
    count = 0
 
    # Find the maximum repeating
    # character starting from str[i]
    res = str[0]
    for i in range(l):
         
        cur_count = 1
        for j in range(i + 1, l):
     
            if (str[i] != str[j]):
                break
            cur_count += 1
 
        # Update result if required
        if cur_count > count :
            count = cur_count
            res = str[i]
    return count
 
# Driver code
if __name__ == "__main__":
 
    str =input('')
    print(maxRepeating(str))