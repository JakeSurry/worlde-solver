#Creates a list of all the words from the words.txt file
words = []
with open('words.txt') as f:
    words = f.readlines()
words = [w.strip() for w in words]

#This dictionary ranks letters based off of how likely they are to apear in the final word,
#These values were found using the letter_frequency.py program
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

#This function is just for getting and organizing the inputs of the user
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

#This is the main loop of the program
for i in range(5):
    correct, present, absent = get_letter_list(correct, present, absent)
    possible = []

    #This is what checks every word in the words.txt file, and compares it to the user information
    for word in words:

        #This makes sure the correct letters are in the word and in the right place
        if len([pair for pair in correct if word[pair[1]] == pair[0]]) == len(correct):

            #This checks if the present letters are in the word, but not where they were initially found
            if len([pair for pair in present if word[pair[1]] != pair[0]]) == len(present) and (set([pair[0] for pair in present]) - set([char for char in word]) == set()) or len(present) == 0:
                
                #This checks to make sure the absent letters aren't in the word
                if not (set([char for char in word]) & set([pair[0] for pair in absent])):
                    possible.append(word)

    #This ranks all of the words in the possible list, and then displays them to the user
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
'''
This project was made by Jake Surry
Thanks for checking it out, hope it is helpful or interesting to you!
'''