def nearestFibonacci(num):
     
    # Base Case
    if (num == 0):
        print(0)
        return
 
    # Initialize the first & second
    # terms of the Fibonacci series
    first = 0
    second = 1
 
    # Store the third term
    third = first + second
 
    # Iterate until the third term
    # is less than or equal to num
    while (third <= num):
         
        # Update the first
        first = second
 
        # Update the second
        second = third
 
        # Update the third
        third = first + second
 
    # Store the Fibonacci number
    # having smaller difference with N
    if (abs(third - num) >abs(second - num)):
        ans =  second
        print(ans)
    elif (abs(third - num) <abs(second - num)):
        ans = third
        print(ans)
    elif (abs(third - num)==abs(second - num)):
        ans=second
        ans1=third
        print(ans,end=' ')
        print(ans1,end=' ')
    # Print the result
 
# Driver Code
if __name__ == '__main__':
     
    N = int(input())
     
    nearestFibonacci(N)