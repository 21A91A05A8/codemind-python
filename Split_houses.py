n = int(input())

name = str(input())

if (n >= 1 & n <= 20):

    if "HH" in name:
    
        print("NO")
    
    elif name == ".":
    
        print("YES")
    
        print("B")
    
    elif name == "H":
    
        print("YES")
    
        print("H")
    
    else:
    
        name = name.replace(".","B")
    
        print("YES")
    
        print(name)