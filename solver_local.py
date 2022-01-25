words = []
with open('words.txt') as f:
    words = f.readlines()
words = [w.strip() for w in words]

letter_frequency = {
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

def get_letter_list(correct, present, absent):
    word = input('List your guess: ')
    correct_letters = input('List all correct letters: ')
    present_letters = input('List all present letters: ')
    absent_letters = input('List all absent letters: ')

    for char in correct_letters:
        itr = [i for (i,c) in enumerate(word) if c == char]
        for i in itr: correct.append((char, i))
    for char in present_letters: 
        itr = [i for (i,c) in enumerate(word) if c == char]
        for i in itr: present.append((char, i))
    for char in absent_letters: absent.append(char)

    return correct, present, absent

correct = []
present = []
absent = []

for i in range(5):
    correct, present, absent = get_letter_list(correct, present, absent)
    possible = []
    for word in words:
        if len([pair for pair in correct if word[pair[1]] == pair[0]]) == len(correct):
            if len([pair for pair in present if word[pair[1]] != pair[0]]) == len(present) and (set([pair[0] for pair in present]) - set([char for char in word]) == set()) or len(present) == 0:
                if not (set([char for char in word]) & set([pair[0] for pair in absent])):
                    possible.append(word)

    if len(possible) > 1:
        best_word = {}
        for word in possible: 
            best_word[word] = sum(letter_frequency[char] for char in set(word))
        if len(possible) < 10:
            top = [sorted(best_word, key=best_word.get, reverse=True)[i] for i in range(len(possible))]
        else:
            top = [sorted(best_word, key=best_word.get, reverse=True)[i] for i in range(10)]
        print(f"\nPossible Words: {', '.join(top)}\n")
    else:
        print(f'\nPossible Words: {possible[0]}\n')
        break

