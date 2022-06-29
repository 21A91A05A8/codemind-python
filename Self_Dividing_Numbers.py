def selfDividingNumbers(left, right):

    # An internal function
    def self_dividing(n):
        # loop through each `n`
        for d in str(n):
            # if it's the first item, or there's no remainder
            if d == '0' or n % int(d) > 0:
                # False
                return False
        # True
        return True

    # Create an `output` to push to
    out = []
    # loop through all items, from the left to the right, inclusive
    for n in range(left, right + 1):
        # if we get a True
        if self_dividing(n):
            # push to the output
            out.append(n)

    #Equals filter(self_dividing, range(left, right+1))
    return out
left=int(input())
right=int(input())
print(*selfDividingNumbers(left, right))