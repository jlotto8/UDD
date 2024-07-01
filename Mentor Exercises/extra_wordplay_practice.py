# write a function that returns true if a word has ONLY the letters in some set of letters (e.g. "ABCD") and false otherwise
"""
create a function that takes a word as a parameter
open the file
use a for loop to go through each word in the file
create a set of the letters to be used
    set a flag to name if letters not in set invalid_letter = False
    use another for loop to go through each letter in each word
    if the letter is not in the set, set the flag to True
    if the letter is in the set, and the flag is false, return 
"""


def is_true(sample_word):
    # file_name = '../Practice Problems/Project Underdog/Wordplay/sowpods.txt'
    # file_name = '../Practice Problems/Wordplay/sowpods.txt'
    # file_handle = open(file_name)

    letters = set(['A','B','C','D'])

    # for word in sample_word:

    invalid_letter = False
    for letter in sample_word:
        if letter not in letters:
            invalid_letter = True
    if letter in letters and invalid_letter == False:
        # print(f'This word: {sample_word} contains only letters in {letters}')
        return True
    return False
print(is_true('CAB'))


