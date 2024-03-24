# What are all of the words that have at least 3 different double letters? 
# For example, “BOOKKEEPER” is an answer to this question because it has a double-O, a double-K, and a double-E.

"""
create a list to hold the result words
create  i, j = 0,1

loop through each word in the file
    create a set to hold double letters
    loop through each letter in each word:
        if j <= len(word)-1:
            using indexes, check if the first letter in the word is the same as the second letter in the word            
                if they are the same, add both letters to the set as a tuple
                    if the len(set) >2:
                        add the word to my results list
                        break
                if the letters are not the same
                    continue
                increment the indexes by 1
print(result list)
"""
file_name = '../../Wordplay/sowpods.txt'
# file_handle = open(file_name)

with open(file_name) as file_handle:
    result_words = []
    for word in file_handle:
        word = word.strip()
        double_letters = set()
        i = 0
        j = 1
        for letter in word:
            if j <= len(word)-1:
                if word[i] == word[j]:
                    double_letters.add((word[i],word[j],))
                i += 1
                j += 1
                if len(double_letters) >2:
                    result_words.append(word)
                    break
    print(result_words)

# if I don't need an else for the if on line 34, do I just ignore it?

# try with for loop in range

    for word in file_handle:
        word = word.strip()  
        double_letters = set()
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                double_letters.add((word[i], word[i + 1]))  # Add tuple of double letters
        if len(double_letters) > 2:  
            result_words.append(word)
    print(result_words)