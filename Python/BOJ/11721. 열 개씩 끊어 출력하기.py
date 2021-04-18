word = input()
words = 'A' + word
for i in range(len(words)):
    if i == 0: continue
    else:
        print(words[i], end='')
    if i % 10 == 0:
        print()