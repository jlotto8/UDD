# Write a function that takes a string phrase and returns a dictionary containing counts of how many times every character appears in phrase.

"""
# create a variable counter, set to 0
create a dict()
loop through the phrase
add each character to the dict()
if the character is in the dict, increase the value of the letter

return dict
"""

# phrase = 'Hello world'
def count_letters(phrase):

    encountered_letters = {}

    for letter in phrase.upper():
        encountered_letters[letter] = encountered_letters.get(letter,0) +1

    return encountered_letters

print(count_letters('Hello World!'))