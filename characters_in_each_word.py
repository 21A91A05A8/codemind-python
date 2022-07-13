s=input()
results = []
for x in s.split():
    word_length = len(x)
    results.append(word_length)
print(*results)