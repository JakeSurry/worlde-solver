import random as rand

words = []
with open('words.txt') as f:
    words = f.readlines()
words = [w.strip() for w in words]

answers = []
with open('answers.txt') as f:
    answers = f.readlines()
answers = [w.strip() for w in answers]

final_word = rand.choice(answers)

alphabet = {
    'a': '\x1b[1;30;47m', 'b': '\x1b[1;30;47m',
    'c': '\x1b[1;30;47m', 'd': '\x1b[1;30;47m',
    'e': '\x1b[1;30;47m', 'f': '\x1b[1;30;47m',
    'g': '\x1b[1;30;47m', 'h': '\x1b[1;30;47m',
    'i': '\x1b[1;30;47m', 'j': '\x1b[1;30;47m',
    'k': '\x1b[1;30;47m', 'l': '\x1b[1;30;47m',
    'm': '\x1b[1;30;47m', 'n': '\x1b[1;30;47m',
    'o': '\x1b[1;30;47m', 'p': '\x1b[1;30;47m',
    'q': '\x1b[1;30;47m', 'r': '\x1b[1;30;47m',
    's': '\x1b[1;30;47m', 't': '\x1b[1;30;47m',
    'u': '\x1b[1;30;47m', 'v': '\x1b[1;30;47m',
    'w': '\x1b[1;30;47m', 'x': '\x1b[1;30;47m',
    'y': '\x1b[1;30;47m', 'z': '\x1b[1;30;47m'}

def out_formatter(word, alphabet):
    win = False
    out = []
    word = [char for char in word]
    final = final_word

    if word == final:
        win = True
    for i, char in enumerate(word):

        if char == final[i]:
            final = f'{final[:i]}0{final[i+1:]}'
            alphabet[char] = '\x1b[1;30;42m'
            out.append([i, char, '\x1b[1;30;42m'])

        elif char in final:
            final = f'{final[:final.find(char)]}0{final[final.find(char)+1:]}'
            if alphabet[char] != '\x1b[1;30;42m': 
                alphabet[char] = '\x1b[1;30;43m'
            out.append([i, char, '\x1b[1;30;43m'])

        else:
            if alphabet[char] == '\x1b[1;30;47m': 
                alphabet[char] = '\x1b[255m'
            out.append([i, char, '\x1b[255m'])

    out = sorted(out, key=lambda x:x[0])

    return out, alphabet, win

def alphabet_out(alphabet):
    print('- - '*16+'-')
    for i, letter in enumerate(alphabet):
        print(f' {alphabet[letter]} {letter.upper()} \x1b[0m ', end='')
        if i == 12:
            print('\n')
    print('\n'+'- - '*16+'-')

def grid_out(grid, i):
    for line in grid:
        for pair in line:
            print(f' {pair[2]} {pair[1].upper()} \x1b[0m ', end='')
        print('\n')

    for j in range(6-i): 
        print(f' \x1b[6;255;47m   \x1b[0m '*5+'\n')

win = False
grid = []

for i in range(6):
    print('')
    alphabet_out(alphabet)
    print('')
    grid_out(grid, i)

    while True:
        guess = input('\n')
        if guess in words and len(guess) == 5:
            break
        else:
            print('Not Valid Word')

    row = guess
    row, alphabet, win = out_formatter(row, alphabet)
    grid.append(row)

print('')
alphabet_out(alphabet)
print('\n')
grid_out(grid, 6)

print(f'\n{final_word}\n')
