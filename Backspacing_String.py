def removeBackspace(s) -> str:
    n = len(s)
    # To point at position after considering the backspaces
    idx = 0
    for i in range(0, n):
        if(s[i] != '#'):
            s = s[:idx] + s[i] + s[idx+1:]
            idx += 1
        elif(s[i] == '#' and idx >= 0):
            idx -= 1
        # This idx can never point at negative index position
        if(idx < 0):
            idx = 0
    ans = ""
    for i in range(0, idx):
        ans += s[i]
    return ans
 
 
# Driver code
s = input()
t = input()
if(removeBackspace(s) == removeBackspace(t)):
      print("True")
else:
    print("False")