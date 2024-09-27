"""
Interview question: rot solver
Part I an example 60 minute interview question. It’s easy to get tripped up on the math — be systematic in your debugging and power through it! Part II is a bonus exercise.

Part I
(If you’ve heard of a rot13 letter substitution cipher, this question is a generalization of that cipher)

Write a function `rot` that:
- takes as arguments: an input string and an amount by which to shift the letters in the string
- returns: the input string, shifted by the shift amount

The function should preserve case — it should be able to handle both upper and lowercase letters — and it should not alter punctuation. The function should support negative numbers. The function should support large shift numbers.

Sample inputs and outputs:
    rot("HELLO", 1) -> "IFMMP" # shift right by 1
    rot("HELLO", 2) -> "JGNNQ" # shift right by 2
    rot("HELLO", -1) -> "GDKKN" # shift left by 1
    rot("HELLO", 27) -> "IFMMP" # shift right by 27, wrapping back to the beginning
    rot("Hello, Rick", 1) -> "Ifmmp, Sjdl" # Preserve case and punctuation
    rot(rot("Hello, Rick", 1), -1) -> "Hello, Rick"

Writing this function will require familiarity with converting between character and ordinals. For example, Python has the `ord` and `chr` functions, and JavaScript has the `charCodeAt` and `fromCharCode` String methods.

You may also find reviewing modular arithmetic (using `%`) to be helpful.

letters = ['a','b','c']

position = (pos + shift) % 26


Pseudocode:

final_string = ""

Loop through input string
    if the character is a letter - isalpha
        check upper or lowercase?
        find position of letter in alphabet first_position = ord(char) - ord('A')
        new_position += (first_position + shift) % 26 
        shifted_char = chr(new_position + ord('A'))
        final_string += shifted_char
    if not a letter:
        final_string += character

encoding - computer's memory of chars is numbers
chr - ASCII
ord - unicode 
"""
def solver(input,shift):

    solved_str = ''
    new_pos_upper = 0
    new_pos_lower = 0
    shifted_pos_upper = 0
    shifted_pos_lower = 0

    for char in input:
        if char.isalpha():
            if char.isupper():
                first_pos_upper = ord(char) - ord('A')
                new_pos_upper = (first_pos_upper + shift) % 26
                shifted_pos_upper = chr(new_pos_upper + ord('A'))
                solved_str += shifted_pos_upper

            elif char.islower():
                first_pos_lower = ord(char) - ord('a')
                new_pos_lower = (first_pos_lower + shift) % 26
                shifted_pos_lower = chr(new_pos_lower + ord('a'))
                solved_str += shifted_pos_lower

        else:
            solved_str += char

    return solved_str  
print(solver('HELLO', 1))


"""
Part II

Using your `rot` function, write a function `decrypt` that takes a text encrypted using a shift substitution cipher of an unknown shift amount, and returns a tuple containing `(the shift used to encrypt the original string, the original string)`.

You will need a dictionary or word list. An input string needs to be long enough to unambiguously determine the the shift used, or there could be multiple valid shifts.

Sample inputs and outputs:

decrypt("Ju xbt uif cftu pg ujnft, ju xbt uif xpstu pg ujnft") -> ("It was the best of times, it was the worst of times", 1)

    
    answer = tuple
put words in a set instead of line by line from the file
break out early if first or 2nd word does not match a word froom the set
consider proper nouns - exception/error ; match %

create a list of each shift possibility
check the first word
check each possible shift


easy way - multiply by -1 to determine position

"""
import string

filename = '../Wordplay/sowpods.txt'

# def get_words(filename):
words = set()
with open(filename) as file:
    # file = file.readlines()

    for line in file:
        line = line.strip()
        # words.add(line.lower())
        words.add(line)
print(words)
    # return words
# print(get_words(sowpods_file_name))

def decrypt(text):
    max_valid_words = 0  
    best_shift = 0  
    decrypted_text = ''  

    for shift in range(26):
        candidate_text = solver(text, -shift) 
        words = candidate_text.split()
        valid_words_count = 0  

        for word in words:
            stripped_word = word.lower().strip(string.punctuation)
            
            if stripped_word in words:
                valid_words_count += 1

        if valid_words_count > max_valid_words:
            max_valid_words = valid_words_count
            best_shift = shift
            decrypted_text = candidate_text

    return decrypted_text, best_shift

print(decrypt("Ju xbt uif cftu pg ujnft, ju xbt uif xpstu pg ujnft"))  

# help with upper and lowercase
# to do - break out early