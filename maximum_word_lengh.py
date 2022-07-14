text = input()
shortest = max(text.split(), key=len)
print(len(shortest))