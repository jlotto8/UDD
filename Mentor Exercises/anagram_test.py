import timeit

def is_anagram(word,word_2):
    word_dict = dict()
    word_2_dict = dict()

    for letter in word:
        word_dict[letter]= word_dict.get(letter,0) +1

    for letter_two in word_2:
        word_2_dict[letter_two] = word_2_dict.get(letter_two, 0) +1
    
    return word_2_dict == word_dict

file_name = '../Practice Problems/Wordplay/sowpods.txt'
# file_name = 'test_file.txt'

with open(file_name) as file_handle:
    largest_anagram_set = set()

    scrabble_words = []
    for line_word in file_handle:
        line_word = line_word.strip()
        scrabble_words.append(line_word)
    print(len(scrabble_words))

    for i in range(len(scrabble_words)):
        current_anagram_set = set()

        for j in range(i+1,len(scrabble_words)):
            word_one = scrabble_words[i]
            word_two = scrabble_words[j]
            
            if is_anagram(word_one, word_two):
                current_anagram_set.add(word_one) 
                current_anagram_set.add(word_two)
                if len(current_anagram_set) > len(largest_anagram_set):
                    largest_anagram_set = current_anagram_set
    # print(largest_anagram_set)

print(timeit.default_timer())


