# What are all of the words that do not have repeated letters?
# Examples:
# The word APPAREL would not be returned because the letter P appears twice
# The word ALERT would be returned because each letter appears only once

"""
create a results list
loop through each word
    strip the words
    set a flag that will become True when a letter already in the set is encountered 
    loop through each letter
        add each letter to a dict
        if the next letter, or any letter in the word is already in dict,
        invalid_letter flag = True
    If invalid_letter
        append to results list
"""

file_name = '../Practice Problems/Wordplay/sowpods.txt'
file_handle = open(file_name)

results = []

for word in file_handle:
    word = word.strip()

    invalid_letter = False

    encountered_letters = {}

    for letter in word:
        encountered_letters[letter] = encountered_letters.get(letter,0) +1

        if encountered_letters[letter] >1:
            invalid_letter = True
            break
    if not invalid_letter:
        results.append(word)
print(results)

# less, command/ctrl f goes forward a page; pager; q to quit; command to run the program, pipe line|less