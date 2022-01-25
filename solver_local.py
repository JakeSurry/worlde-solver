words = []
with open('words.txt') as f:
    words = f.readlines()
words = [w.strip() for w in words]

words = [word for word in words if len(word) == 5]

letter_frequency = {
    'a': .078,
    'b': .02,
    'c': .04,
    'd': .038,
    'e': .11,
    'f': .014,
    'g': .03,
    'h': .023,
    'i': .082,
    'j': .0021, 
    'k': .025,
    'l': .053,
    'm': .027,
    'n': .072,
    'o': .061,
    'p': .028,
    'q': .0024,
    'r': .073,
    's': .087,
    't': .067,
    'u': .033,
    'v': .01,
    'w': .0091,
    'x': .0027,
    'y': .016,
    'z': .0044
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

