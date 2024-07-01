# [ ] Finding alphabet chains:
#     - First, what are all of the words that have a least one “A”, one “B”, one “C”, one “D”, one “E”, and one “F” in them, in any order?
#         - For example, “FEEDBACK” is an answer to this question
    # - Part 2, is “ABCDEF” the longest alphabet chain that can be found in a word, or is there a longer chain starting somewhere else in the alphabet? Find the longest chain and the words that can be made from that chain.

def find_letters_in_max_chain(words):
    max_chain_letters = set()
    max_length = 0 

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