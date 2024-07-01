# given a word, print a dictionary with number of times each letter appears in that word. For example, banana -> {a: 3, b: 1, n: 2}
# bonus follow-up: print whether two words are anagrams of each other. Hint: they are anagrams if their letter counts are the same; e.g. the letter counts for "paces" and "space" are both {a: 1, c: 1, e: 1, p: 1, s:1}


dict_of_word = {}

word = 'paces'
word_2 = 'space'

for letter in word:
    if letter in dict_of_word:
        dict_of_word[letter] += 1
    else:
        dict_of_word[letter] = 1

dict_of_word_2 = dict()

for char in word_2:
    if char in dict_of_word_2:
        dict_of_word_2[char] += 1
    else: 
        dict_of_word_2[char] = 1

if dict_of_word == dict_of_word_2:
    print(True)
else:
    print(False)
