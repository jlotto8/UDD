# What is the longest word that can be made without the letters in “AEIOSHRTN” (in other words, without the most common letters)? Make sure your solution can handle ties.

"""
create a set to hold the letters not to use
create a helper function to check if the letters are valid
loop through each word
    loop through each letter
        if letter is in the set the word is not valid
create a list to hold the longest words 
create a variable to hold the longest word length initialize to 0
loop through all the valid words
if a word is longer than longest word, longest word becomes that word length; variable get reset
results = [word]
check if the length of the word is == current longest word
or if it is > the current longest word
    if either of theses are True, add them results list
"""
file_name = '../../Wordplay/sowpods.txt'
file_handle = open(file_name)
results = []
invalid_letters = set('AEIOSHRTN')

current_longest_word = 0

for word in file_handle:
    word = word.strip()

    valid_letter = True
    
    for letter in word:
        if letter in invalid_letters:
            valid_letter = False

    if valid_letter:
        if len(word) > current_longest_word:
            current_longest_word = len(word)
            results = [word]
        elif len(word) == current_longest_word:
            results.append(word)

print(results)

# file_name = 'test_words.txt'
# file_handle = open(file_name)

# results = []
# invalid_letters = set('AEIOSHRTN')

# current_longest_word = 0

# for word in file_handle:
#     word = word.strip()

#     valid_letter = True
    
#     for letter in word:
#         if letter in invalid_letters:
#             valid_letter = False

#     if valid_letter:
#         if len(word) > current_longest_word:
#             current_longest_word = len(word)
#             results = [word]
#         elif len(word) == current_longest_word:
#             results.append(word)

# print(results)