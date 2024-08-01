# What are all of the words that have only “E”s for vowels and are at least 15 letters long?


file_name = '../../Wordplay/sowpods.txt'
file_handle = open(file_name)

invalid_vowels = ['A','I','O','U','Y']
results_list = []

"""
create a list of invalid vowels
create a results list

loop through each word in the file
    create a flag to note when I find an invalid vowel
    loop through each letter in each word
        if char in invalid vowels, set the flag to True
        check that each word contains 'E'
        check that each word >14 characters
        if flag == False, and 'e' in the word, and length is >14 chars:
            add the word to a list
"""

for line in file_handle:
    line = line.strip()

    found_invalid_vowels = False
    for char in line:
        if char in invalid_vowels:
            found_invalid_vowels = True
    if len(line) >14 and 'E' in line and found_invalid_vowels == False:
        results_list.append(line)
print(results_list)
