# What are all of the words that have only “U”s for vowels?

"""
create a list of vowels, excluding 'u'
loop through each word in the file
    create a flag for invalid chars set to false
    loop through char in each word
        check if char is not in list of vowels,
        if I find a letter that is invalid, set the flag to True

        check if 'u' is a character in the word
    if word contains 'U' and the chars are not in the list of vowels, and flag is False
        add word to a new list
"""
# be careful and check conditionals to see if they are doing what I intended

file_name = '../../Wordplay/sowpods.txt'
file_handle = open(file_name)

vowels = ['A','E','I','O','Y']
u_vowels_word_list = []

for line in file_handle:
    line = line.strip()

    found_invalid_letter = False
    for char in line:
        # print(line)       
        if char in vowels:
            found_invalid_letter = True
            # print(found_invalid_letter, char)
    if found_invalid_letter == False and 'U' in line:
        # print(line)
        u_vowels_word_list.append(line)
print(u_vowels_word_list)
