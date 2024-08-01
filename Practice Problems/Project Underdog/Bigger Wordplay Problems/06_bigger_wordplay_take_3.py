def find_longest_chain_letters(words):
    max_chain_letters = set() 

    # Iterate through each word in the list of words
    for word in words:
        sorted_word = sorted(word) 
        current_chain_letters = []
        previous_letter = ' '  

        # Iterate through each letter in the sorted word
        for letter in sorted_word:
            if ord(letter) - ord(previous_letter) == 1:
                current_chain_letters.append(letter)  
            else:
                current_chain_letters = [letter]  # Start a new chain if sequence is broken
            previous_letter = letter

            if len(current_chain_letters) > len(max_chain_letters):
                max_chain_letters = set(current_chain_letters)

    return sorted(max_chain_letters)

def find_words_with_chain(file_name, chain_letters):
    valid_words = []

    with open(file_name) as file_handle:
        for line in file_handle:
            word = line.strip()
            # Check if the word contains all letters from the chain
            if all(letter in word for letter in chain_letters):
                valid_words.append(word)

    return valid_words

file_name = '../../Wordplay/sowpods.txt'
with open(file_name) as file_handle:
    words = [line.strip() for line in file_handle]

# Find the letters in the longest chain within the words
max_chain_letters = find_longest_chain_letters(words)

# Find words containing the letters in the longest chain
valid_words = find_words_with_chain(file_name, max_chain_letters)

# Print the results
print("Longest Chain Letters:", max_chain_letters)
print("Number of Longest Chain Letters:", len(max_chain_letters))
print("Valid Words with Longest Chain Letters:", valid_words)
print("Number of Valid Words:", len(valid_words))
