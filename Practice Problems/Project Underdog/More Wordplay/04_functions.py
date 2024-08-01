# Write a function that takes a string word as an argument and returns a count of all of the “A”s in that string.
import sys

"""
create a variable counter; initialize it to 0
loop through each letter in the word
    if letter == A
    accumulate the counter
    
return the accumulator
"""

def count_a_letter(word):

    number_of_letter_a = 0

    for letter in word:
        if letter == 'A':
            number_of_letter_a += 1
    
    return number_of_letter_a

# for name in sys.argv[1:]:
print(count_a_letter(name))

# list of arguments my program was run with; 