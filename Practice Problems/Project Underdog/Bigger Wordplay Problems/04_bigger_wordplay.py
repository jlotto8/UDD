# Write a function that takes a string availableLetters as an argument and returns an array of all of the words that can be made from only those letters. 
# Letters can be re-used as many times as needed and can appear in any order. Not all of the letters in availableLetters have to be used/?????

'''
create a set of result words
create a an empty list with each letter in each word

loop through the word
    create a flag invalid letters, which will turn True when a letter from a word is not in the list
    add each letter of the word to a list

        loop through each word in the file
            check if letter from the list of letters is in the word
            check that the letters in the word are not invalid flag = False
            if the letters in the word from the file are the in the list of letters, and the letters are not invalid
            add the word to the results set
return the results set
'''


def find_words(available_letters):
    file_name = '../../Wordplay/sowpods.txt'
    with open(file_name) as file_handle:
        result_words = set()
        letters = set() #['H','E','L','L','O']

        for letter in available_letters:
            letter = letter.upper()
            letters.add(letter)
        

        for word in file_handle:
            word = word.strip()
            invalid_letter = False

            for char in word:
                if char not in letters:
                    invalid_letter = True
                    break
            if invalid_letter == False:
                result_words.add(word)
        return result_words
    
print(find_words('abcde'.upper()))


list_of_letters = ['H','E','L','L','O']

"""
CAROUSEL
HELL

check if the letters in the words are in the list of letters 
check if the letters in the words are not in the list of letters

loop through each word in the file
    create a flag for invalid letter, when a letter in the word is not in the letters list
    
    loop through each letter in the word
"""

# I did it! Over 2 days, 2 hours total taking breaks :(
