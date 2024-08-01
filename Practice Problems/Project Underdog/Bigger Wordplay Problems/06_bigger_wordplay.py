# [ ] Finding alphabet chains:
#     - First, what are all of the words that have a least one “A”, one “B”, one “C”, one “D”, one “E”, and one “F” in them, in any order?
#         - For example, “FEEDBACK” is an answer to this question
    # - Part 2, is “ABCDEF” the longest alphabet chain that can be found in a word, or is there a longer chain starting somewhere else in the alphabet? Find the longest chain and the words that can be made from that chain.

"""
Part 1 check if a word has ABCDEF
loop through the letters in the word
    if the letter is in the set of required letters
        add the letter to the new set
        check if both sets are equal
          
Paart 1 to find the words that have ABCDEF
results list to save the words that have ABCDEF
create a function pass in filename as parameter
loop through each word in the file
    strip the word
    use helper function 
    if true:
        add word to the result list
return the list of words that contain ABCDEF


Part 2
test_word = 'FEEDBACK' 
*if a chain exists, are there any words that have that chain in them*

input - word
output - len(chain), words that are that length with letters in that chain
        if no letters in the chain, return len(0)

the longest chain known is len(6) ABCDEF 
create function, pass in the file as parameter
loop through each word in the file
    loop through each letter in the word
        loop through each letter in the word again? to compare the previous letter to the next, and keep increasing the length

test_word = 'monkey'
find the biggest chain in the word
put the word in a set
cast the set to a list
sort the list
(e,k,m,n,o,y)
find the longest chain in a word

(d,i,m,n,o,r,s,t,u,w)
current_chain_length = 3, m,n,o; 
max_chain_length = 4, r,s,t,u
current_chain_letters = mno
max_chain_letters = rstu 

check each letter in the word, from left to right, name two variables- the first letters, and the second letter in the word
check the value of the second letter - the first letter through the whole word
if the value == 1
it is a chain
increment the chain

if the value is not == 1
save the length of current chain
and keep checking the difference in value of next letter - previous letter, starting over at 1

create a separate function to find the words that have the longest chain
"""
alphabet = ['A','B','C','D','E','FGHIJKLMNOPQRSTUVWXYZ']

def have_required_letters(test_word):
    required_letters = set('ABCDEF')
    test_word_letters_set = set()

    for char in test_word:
        if char in required_letters:
            test_word_letters_set = set(test_word)
    return required_letters.issubset(test_word_letters_set)


def find_words_with_abcdef(filename):
    with open(filename) as file_handle:

        abcdef_result_words = set()

        for line in file_handle:
            line = line.strip()
            if have_required_letters(line) == True:
                abcdef_result_words.add(line)

        return abcdef_result_words

def find_letters_in_max_chain(words):
    max_chain_letters = set()

    for word in words:
        test_word_set = set(word)
        test_word_list = list(test_word_set)
        sorted_word = sorted(test_word_list)
        previous_letter = ' '
        current_chain_letters = set()
       
        for letter in sorted_word:
            if ord(letter) - ord(previous_letter) == 1:
                current_chain_letters.add(previous_letter)
                current_chain_letters.add(letter)
            else:
                current_chain_letters.clear()
            previous_letter = letter

        if len(current_chain_letters) > len(max_chain_letters):
            max_chain_letters = current_chain_letters.copy()

    return sorted(max_chain_letters)
# print(find_letters_in_max_chain('../../Wordplay/sowpods.txt'))

# def find_max_chain_and_words(file_path):
#     max_chain_length = 1
#     words_with_max_chain = []

#     with open(file_path, 'r') as file:
#         for line in file:
#             word = line.strip()
#             sorted_word = ''.join(sorted(word))  # Sort the letters in the word
#             current_chain = 1
#             previous_letter = 'A'  # Start from 'A' for each word

#             for letter in sorted_word:
#                 if ord(letter) - ord(previous_letter) == 1:
#                     current_chain += 1
#                 else:
#                     if current_chain == max_chain_length:
#                         words_with_max_chain.append(word)
#                     elif current_chain > max_chain_length:
#                         max_chain_length = current_chain
#                         words_with_max_chain = [word]
#                     current_chain = 1  # Reset current_chain if the chain is broken
#                 previous_letter = letter

#             if current_chain == max_chain_length:
#                 words_with_max_chain.append(word)
#             elif current_chain > max_chain_length:
#                 max_chain_length = current_chain
#                 words_with_max_chain = [word]

#     max_chain_letters = find_letters_in_max_chain(words_with_max_chain)

#     return max_chain_length, max_chain_letters, words_with_max_chain

# print(find_max_chain_and_words('../../Wordplay/sowpods.txt'))
# find_words_with_max_chain()

# words_with_max_chain = find_words_with_max_chain(file_path, max_chain_length)
# finish for homework; add an else ctrl d - end a file early return false
