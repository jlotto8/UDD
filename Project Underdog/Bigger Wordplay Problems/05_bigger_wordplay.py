# [ ] What are all of the compound words? These are words made up of 2 smaller words. For example, “SNOWMAN” is a compound word made from “SNOW” and “MAN”, and “BEACHBALL” is a compound word made from “BEACH” and “BALL”.

"""
subset? look up- if more than one word in the file is in the word:
    the word is a compound word
    add the word to the results set

create a set to hold the results

loop through the file
    loop through the file again -  i need to compare each word to every other word in the file to see if it contains another word
        check if there are > 1 word from the file in the word 
            if yes, add the word to the results list
            if no, continue
print the result set
# this output is not correct - example - first word 'AA' is in lots of words, but those words are not compound words
new plan
# growing window

all the letters in the word need to be in the 2 smaller substrings
loop through each word
    loop through each letter using indexes check if the substring is a word 
        check if each substring is a word in the list
        if a substring is found, [0:4] 
        if not, keep checking the rest of the word; is the remainder of the word also a word

"""
# word = 'snowman'  word_2 = beachballs, beach, ball, balls
# test_word = 'aaabbbc'
# aaa 
# 'bbb'
# bbbc

# word = 'beachball'
# for i in range(len(word)+1):
    # print(word[i])
    # print(word[:i]) # prints first substring
    # print(word[]) # print remainder substring
    

file_name = '../../Wordplay/sowpods.txt'
with open(file_name) as file_handle:

    result_words = set()
    all_words = set('SNOWMAN', 'BACKPACK','HELLO','HI','FEEDBACK', 'SNOW','MAN','BACK','PACK')

    for word in file_handle:
        word = word.strip()
        all_words.add(word)


        for i in range(1,len(word)):
            if word[:i] in all_words and word[i:] in all_words:
                # print(word[:i], word[i:])
                result_words.add(word)
    print(result_words)

    #output is large, not traditional 'compound words' 

    # check a smaller list of words against the scrabble list