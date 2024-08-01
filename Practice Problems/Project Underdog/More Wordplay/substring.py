# Functions

# [ ] Write a function that takes a string `substring` as an argument and returns an array of all of the words that contain that substring (the substring can appear anywhere in the word).


"""
loop through each word

if substring in word
if yes, add the words to a list
"""

def find_substring(substring):

    file_name = '../../Wordplay/sowpods.txt'
    file_handle = open(file_name)

    results = []

    results = [word.strip() for word in file_handle if substring in word]
    # for word in file_handle:
    #     word = word.strip()

    #     if substring in word:
    #         results.append(word)
    return results

print(find_substring('FULL'))

# review list comprhension, filter, map