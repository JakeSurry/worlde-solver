words = []
with open('words_alpha.txt') as f:
    words = f.readlines()
words = [w.strip() for w in words]

print(f'{len(words)}\n')


words = [word for word in words if len(word) == 5]
new_words = []

for word in words:
    unique = True
    if word.isalpha():
        for char in word:
            if word.count(char) > 1:
                unique = False
                break
        if unique:
            new_words.append(word)

i = 0
while True:
    unique_words = []
    unique_words.append(new_words[i])

    for word in new_words:
        unique = True
        for unique_word in unique_words:
            if (set([char for char in word]) & set([char for char in unique_word])):
                unique = False
                break
        if unique:
            unique_words.append(word)
    if len(unique_words) >= 5:
        break
    else:
        i += 1
        print(f'{i/len(new_words)*100}%', end = '\r')

print(unique_words)
