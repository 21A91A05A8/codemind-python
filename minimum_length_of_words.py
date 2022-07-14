text = input()
shortest = min(text.split(), key=len)
print(len(shortest))