"""
Find the largest group of words in the scrabble dictionary that are anagrams of each other. For example, ["eat", "ate", "tea"] are all anagrams of each other.

Idea 1: 
if I'm comparing 2 words: eat, ate - add each letter to a dictionary per word, with a letter count of each letter as the value word1 = {'e': 1, "a":1, 't';1}, word2 = {'t':1, 'e':1, 'a';1}

then compare each dictionary to the others to check if they are equal, if they are, the words are anagrams
if they are anagrams, add the word to a results list

if duplicate letters do not matter for the output, each word could be added to a set, and the sets checked for equality to determine if a word is an anagram 

problems - this requires another DS to hold thousands of dictionaries ( 1 dictionary per word)
-  I have to somehow compare each word in the scrabble word list to every other word, and keep a list of all the anagram words, and the length of that list. If there are a group of words longer than the current list of words, I throw that list away, and save the new list of words that are anagrams of each other

-think about keys and values

implementation - break this problem down into at least 2 different functions:
a. function to determiine if words are anagrams of each other
b. function to find the largest group of words that are anagrams of each other

a. 
create a function that takes 2 words as parameters
create 2 dictionaries, 
loop through each word
    check if the letter is in the dict
        if it is, incremment the count by 1, if not set count to 0
compare the 2 dictionaries for equalilty, if they are the same:
return True, else return False

The above solution takes too long for such large input. 

There’s an O(n) solution to this, that depends on being able to answer “Is this word an anagram of a word I’ve previously seen” in O(1) time.
Some leading questions:
what are some things you can do in O(1) time to answer that question?  Definitely not a loop over all previous words!
if you made a dictionary or a set of all the previous words, what could you use as the key?

# sort words, add as keys

all previously seen words - add word to a dictionary as the key, and a set of all the words that are anagrams of that word as the value 

"""
import timeit

# def is_anagram(word,word_2):
#     word_dict = dict()
#     word_2_dict = dict()

#     for letter in word:
#         word_dict[letter]= word_dict.get(letter,0) +1

#     for letter_two in word_2:
#         word_2_dict[letter_two] = word_2_dict.get(letter_two, 0) +1
    
#     return word_2_dict == word_dict

# with open(file_name) as file_handle:
#     largest_anagram_set = set()

#     scrabble_words = []
#     for line_word in file_handle:
#         line_word = line_word.strip()
#         scrabble_words.append(line_word)

#     for i in range(len(scrabble_words)):
#         current_anagram_set = set()

#         for j in range(i+1,len(scrabble_words)):
#             word_one = scrabble_words[i]
#             word_two = scrabble_words[j]
            
#             if is_anagram(word_one, word_two):
#                 current_anagram_set.add(word_one) 
#                 current_anagram_set.add(word_two)
#                 if len(current_anagram_set) > len(largest_anagram_set):
#                     largest_anagram_set = current_anagram_set
#     print(largest_anagram_set)
# print(timeit.default_timer())
file_name = '../Practice Problems/Wordplay/sowpods.txt'
# file_name = 'test_file.txt'
with open(file_name) as file_handle:

    largest_anagram_set = set()
    anagrams = dict()

    for word in file_handle:
        word = word.strip()

        sorted_word = ''.join(sorted(word))

        if sorted_word in anagrams:
            anagrams[sorted_word].add(word)
        else:
            anagrams[sorted_word] = {word}
    print(anagrams[sorted_word].values())
    


print(timeit.default_timer())