"""
This was a real interview question at Dropbox. Candidates who passed the interview would typically successfully implement Part 1 and then articulate an algorithm for Part 2 within 60 minutes, but they might not have time to implement Part 2.

Part 1

Write code that:

- Accepts a string (e.g. as an argument to a function, or as a command-line argument). This string represents your Scrabble “rack”.
- Prints out the words that can be made from the characters in that input string, along with their Scrabble scores, one word per line, in descending score order

Example input and output:

`$ python scrabble_cheater.py SPCQEIU  # Use any language you like.`
`17 piques`
`17 equips`
`16 quips`
`16 pique`
`16 equip`
`15 quip`
`…`

Resources:
- Word list
- Letter scores

Key points:

- Letters cannot be reused. For example, if your Scrabble rack is “ABCD”, you can make the word “CAB” but not the word “DAD”, because you only have one “D”.
- 
Part 2

Extend the script to handle blank tiles. When reading the input, the character _ can be used as a wildcard — it can represent any letter.

Wildcards do not count towards a word's score.

blanks - count how many there are
look through letters  in  rack
if yes, remove them
if blank decrement the count
keep track of tiles used to get score
"""

sowpods_file_name = '../Wordplay/sowpods.txt'
# letter_scores_file_name = 'letter_scores.txt'
# # file_handle = open(sowpods_file_name)

# with open(letter_scores_file_name) as file_handle:

    
# Define the letter scores
scores = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1,
    "F": 4, "G": 2, "H": 4, "I": 1, "J": 8,
    "K": 5, "L": 1, "M": 3, "N": 1, "O": 1,
    "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1,
    "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
}

# Load the word list
def load_word_list(filename):
    words = []
    with open(filename, 'r') as file:
        for line in file:
            words.append(line.strip())
    return words

# Check if a word can be made from the rack # pepper #abcd_ _
def can_make_word(word, rack):
    rack_list = list(rack)  # Convert rack to a list to manipulate it
    
    for letter in word:
        if letter in rack_list:
            rack_list.remove(letter)  # Remove the letter from the rack list
        else:
            return False  # If a letter is missing or not enough, return False
    return True  # If all letters are matched, return True

# Calculate the score for a word
def calculate_score(word):
    score = 0
    for letter in word:
        score += scores[letter]
    return score

# Find valid words and their scores
def find_scrabble_words(rack, word_list):
    valid_words = []
    for word in word_list:
        if can_make_word(word, rack):
            word_score = calculate_score(word)
            valid_words.append((word, word_score))
    
    # Use a different sort, sort()
    # Sort valid_words by score in descending order; lamda 
    for i in range(len(valid_words)):
        for j in range(i + 1, len(valid_words)):
            if valid_words[i][1] < valid_words[j][1]:
                valid_words[i], valid_words[j] = valid_words[j], valid_words[i]
    
    return valid_words



# Main function
def main():
    rack = input("Enter your Scrabble rack: ").upper()
    
    word_list = load_word_list('../Wordplay/sowpods.txt')
    
    # Find valid words
    words_with_scores = find_scrabble_words(rack, word_list)
    
    if not words_with_scores:
        print("No valid words found.")
    else:
        for word, score in words_with_scores:
            print(f"{score} {word}")

if __name__ == "__main__":
    main()

    
#     # Print the results
#     if not words_with_scores:
#         print("No valid words found.")
#     else:
#         for word, score in words_with_scores:
#             print(f"{score} {word}")

# if __name__ == "__main__":
#     main()


"""
part 2 blanks
Function: Generate Words

    Start with an empty set to store results.
    Begin generating words by calling a helper function with the initial letters and an empty string as the current word.

Helper Function: Generate Words Recursively

    If there are no more letters to process:
    Check if the current word is valid.
    If valid, add it to the results set.
Else:
    Take the next letter from the remaining letters.
    If the letter is a wildcard (_):
        For each possible letter (A to Z):
            Recursively generate words by replacing the wildcard with each letter.
    If the letter is not a wildcard:
        Add the letter to the current word.
        Recursively continue with the next letter.

Calculate Score Function

    start a counter
    loop through each letter in word
        if letter is not a wildcard, add it's value to the score

Vaildate Word Function
    check if word is valid
    return true or false


"""