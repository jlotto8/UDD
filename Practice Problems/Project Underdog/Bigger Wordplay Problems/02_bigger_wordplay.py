# What are all of the words that are at least 8 letters long and use 3 or fewer different letters? 
# For example, “REFERRER” is an answer to this question, because it uses only 3 different letters: R, E, and F.÷

"""
create a set to hold the results- output of words that are >7 letters, and only use 3 or less letters
if len(set) <= 3
add the word to the results list

loop through each word
    if len(word) >7:
        create an empty set
        create a flag invalid_length = False
        loop through each letter in each word
            if letter not in set
                add the letter
            if letter is already in set
                set flag to True
                break
        if flag == false and len(set) < 4:
            add word to results set
print results
"""

file_name = '../../Wordplay/sowpods.txt'
file_handle = open(file_name)

result_words = set()

for word in file_handle:
    word = word.strip()

    letters_set = set()
    duplicate_letter = False
    for letter in word:
        if letter not in letters_set:
            letters_set.add(letter)
        # else:
        #     duplicate_letter = True
        #     break
    if letter in letters_set and len(letters_set) < 4:
        if len(word) > 7: 
            result_words.add(word)
print(result_words)

# did this independtently! Took 3 hours. I had 1-2 logical errors. 