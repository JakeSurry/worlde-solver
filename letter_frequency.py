'''

---------------------------------------------------------------
This section was to create my custom letter freuqeuncy rankings
---------------------------------------------------------------

'''

words = []
with open('words.txt') as f:
    words = f.readlines()
words = ''.join([w.strip() for w in words])

letter_frequency = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}

for char in letter_frequency: letter_frequency[char] = round((words.count(char)/len(words)), 5)

print(letter_frequency)

new_dic = {
    'a': 0.09235, 
    'b': 0.02508, 
    'c': 0.03127, 
    'd': 0.03782, 
    'e': 0.10271, 
    'f': 0.01719, 
    'g': 0.02535, 
    'h': 0.02714, 
    'i': 0.05796, 
    'j': 0.00449, 
    'k': 0.02320, 
    'l': 0.05197, 
    'm': 0.03047, 
    'n': 0.04551, 
    'o': 0.06842, 
    'p': 0.03113, 
    'q': 0.00173, 
    'r': 0.06411, 
    's': 0.10276, 
    't': 0.05080, 
    'u': 0.03871, 
    'v': 0.01070, 
    'w': 0.01602, 
    'x': 0.00444, 
    'y': 0.03198, 
    'z': 0.00669
    }

'''

--------------------------------------------------------
This section was to find the best possible starting word 
--------------------------------------------------------

'''

with open('words.txt') as f:
    words = f.readlines()
words = [w.strip() for w in words]

best_word = {}
for word in words: 
    best_word[word] = sum(new_dic[char] for char in set(word))

best_word = sorted(best_word, key=best_word.get, reverse=True)[0]

print(best_word)
