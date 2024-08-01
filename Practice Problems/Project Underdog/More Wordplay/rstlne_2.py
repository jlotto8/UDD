# What is the longest word that can be made from only the letters in “RSTLNE”? Not all of those letters need to be used, and letters can be repeated. Make sure your solution can handle ties.

"""
create a set with valid letters = 'RSTLNE'
create a variable to represent the length of each word  longest_word_length = 0

loop through each word
    
    create a flag to alert when a letter is not valid- meaning the letter is not in valid letters
    
    loop through each letter in each word
        if the letter is not in valid letters
            set the flag to True invalid_letter
            break

    if the letter is in valid 
        if length of the word == longest word
        if length of the word is > longest word:
        if length of the word is < longest word
        longest_word gets reset to the length of that word
        
    if the lengh of the word <= longest_word and the letter is in valid letters and invalid_char == False:
        result.append(line)

keep track of the length of each longest word, and the word itself, and if the word is valid (all letters)
chaining conditionals can be a bad idea
if
    if
"""

file_name = '../../Wordplay/sowpods.txt'
file_handle = open(file_name)

results = []
letters = ['R','S','T','L','N','E']
max_word_length = 0

for word in file_handle:
    word = word.strip()

    valid_letter = True
    for letter in word:
        if letter not in letters:
            valid_letter = False
    if valid_letter:
        if len(word) > max_word_length:
            max_word_length = len(word)
            results = [word]
        elif len(word) == max_word_length:
            results.append(word)
print(results)


