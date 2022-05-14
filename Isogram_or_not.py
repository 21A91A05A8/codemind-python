def check_isogram(str1):
    return len(str1) == len(set(str1.lower()))

print(check_isogram(input('')))