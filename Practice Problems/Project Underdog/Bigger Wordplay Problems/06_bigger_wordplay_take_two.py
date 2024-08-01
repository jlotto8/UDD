# def find_letters_in_max_chain(words):
#     max_chain_letters = set()

#     for word in words:
#         word = word.strip()

#         current_chain_letters = []
#         previous_letter = ' '
#         for letter in sorted(word):
#             if ord(letter) - ord(previous_letter) == 1:
#                 current_chain_letters.append(letter)
#             else:
#                 current_chain_letters = [letter]  # Start a new chain if sequence is broken
#             previous_letter = letter

#             if len(current_chain_letters) > len(max_chain_letters):
#                 max_chain_letters = set(current_chain_letters)

#     return sorted(max_chain_letters)


def find_letters_in_max_chain(test_word):
    max_chain_letters = set()
    file_name = '../../Wordplay/sowpods.txt'
    with open(file_name) as file_handle:

        for line in file_handle:
            word = line.strip()
            current_chain_letters = []
            previous_letter = ' '
            for letter in sorted(word):
                if ord(letter) - ord(previous_letter) == 1:
                    current_chain_letters.append(letter)
                else:
                    current_chain_letters = [letter]  # Start a new chain if sequence is broken
                previous_letter = letter

                if len(current_chain_letters) > len(max_chain_letters):
                    max_chain_letters = set(current_chain_letters)

    return sorted(max_chain_letters)
find_letters_in_max_chain('ABBC')

def find_max_chain_and_words(test_word):
    max_chain_length = 1
    words_with_max_chain = []

    # with open(file_path, 'r') as file:
    for line in test_word:
        word = line.strip()
        sorted_word = sorted(word)  # Sort the letters in the word
        current_chain = 1
        previous_letter = ' '  # Start from an empty string with one space for each word

        for letter in sorted_word:
            if ord(letter) - ord(previous_letter) == 1:
                current_chain += 1
            else:
                if current_chain == max_chain_length:
                    words_with_max_chain.append(word)
                elif current_chain > max_chain_length:
                    max_chain_length = current_chain
                    words_with_max_chain = [word]
                current_chain = 1  # Reset current_chain if the chain is broken
            previous_letter = letter

        if current_chain == max_chain_length:
            words_with_max_chain.append(word)
        elif current_chain > max_chain_length:
            max_chain_length = current_chain
            words_with_max_chain = [word]

    max_chain_letters = find_letters_in_max_chain(words_with_max_chain)

    return max_chain_length, max_chain_letters, words_with_max_chain
# print(find_max_chain_and_words('ABBC'))
print(find_max_chain_and_words('../../Wordplay/sowpods.txt'))
"""
abbc
longest_chain = 'abc' len = 3

max chain length
letters in that chain
find all the words that can be made from that chain

'FEEDBACK' 
'abcdef' 'jklmn'

break this down into 2 different functions

alphabet_chain = set('abcdef') 
seen = set(abcdefgx)

find words that contain those letters (can have other letters too)

test_word = 'bacdefxg'


sorting is not needed
l = ['bacdefxg']


try again - sorting not needed; if I put letters in order in array 
"""
