# Step 1: Define the letter scores
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

# Check if a word can be made from the rack
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
    
    # Sort valid_words by score in descending order
    for i in range(len(valid_words)):
        for j in range(i + 1, len(valid_words)):
            if valid_words[i][1] < valid_words[j][1]:
                valid_words[i], valid_words[j] = valid_words[j], valid_words[i]
    
    return valid_words

# Main function
def main():
    # Prompt the user for input
    rack = input("Enter your Scrabble rack: ").upper()
    
    # Load the word list
    word_list = load_word_list('../Wordplay/sowpods.txt')
    
    # Find valid words
    words_with_scores = find_scrabble_words(rack, word_list)
    
    # Print the results
    if not words_with_scores:
        print("No valid words found.")
    else:
        for word, score in words_with_scores:
            print(f"{score} {word}")

if __name__ == "__main__":
    main()
