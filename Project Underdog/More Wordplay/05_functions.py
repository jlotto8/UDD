# Write a function that takes a string word as the first argument, a string letter as the second argument, and returns a count of how many times letter occurs in word.
import sys

"""

"""

def count_letter(word,letter):

    number_of_letter = 0

    for char in word:
        if char == letter:
            number_of_letter += 1
    
    return number_of_letter

# for name in sys.argv[1:]:

# print(count_letter('HELLO','L'))
print(count_letter(sys.argv[1],sys.argv[2]))

# zsh/bash compatible, bash cheatsheet 