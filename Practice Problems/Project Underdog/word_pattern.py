"""
Hard interview question: Word Pattern
This is a retired 60-minute coding question from Dropbox. A good goal would be to be able to finish Part 1 within the 60 minutes, and then to come up with a plan for Part 2 even if you don’t have time to implement it fully.

Part 1
Write a function that takes as arguments two strings: `pattern` and `input`. Return whether or not the words in `input` match the pattern of the characters in `pattern`.

Example 1:
| `pattern: 'abba'`            |
| `input: 'red blue blue red'` |
| `result: True`               |

Example 2:
| `pattern: 'abcabc'`                      |
| `Input: 'red blue green red blue green'` |
| `result: True`                           |

Example 3:
| `pattern: 'abba'`             |
| `Input: 'red blue green red'` |
| `result: False`               |

Part 2

Write a function that takes as arguments two strings: `pattern` and `input`. Return whether or not `input` can be broken into words to match the pattern of the characters in `pattern`.

(In other words, this is the same problem as part 1, but `input` doesn’t contain spaces, so you’ll need to determine if it is possible to split up the input into words in a way that matches `pattern`. You will likely want to use recursion.)

Example 1:
| `pattern: 'abcba'`             |
| `input: 'redbluegreenbluered'` |
| `result: True`                 |

Example 2:
| `pattern: 'aba'`                                                               |
| `Input: 'xxyyyxx'`                                                             |
| `result: True`, with multiple solutions:<br><br>- x, xyyyx, x<br>- xx, yyy, xx |

Example 3:
| `pattern: 'abba'`          |
| `Input: 'redbluegreenred'` |
| `result: False`            |

letters to words bindings

part 1

dictionary 
key is the letter in the pattern
value is the word in the input string

part 2 
"""

def is_pattern(pattern, words):

    # pattern = list(pattern)
    words = words.split()

    char_to_word = dict()
    
    # If the number of pattern characters doesn't match the number of words, return False
    if len(pattern) != len(words):
        return False

    for i in range(len(pattern)):
        char = pattern[i]  
        word = words[i]   
        
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            # if the word is already assigned to another character, return False
            if word in char_to_word.values():  # O(n**2)
                return False
            
            # otherwise, add the character to the current word
            char_to_word[char] = word
    
    return True

# print(is_pattern('abba', 'red blue blue red'))  
# print(is_pattern('abcabc', 'red blue green red blue green'))  
# print(is_pattern('abba', 'red blue green red'))  
# print(is_pattern('abc', 'dog dog dog'))  

"""
part 2

Example 1:
| `pattern: 'abcba'`             |
| `input: 'redbluegreenbluered'` |
| `result: True`                 |

bind the smallest input first

recursive function: 
params(pattern, input)
(pattern_index, word_index, dict) set these to empty/0
can also use the shortened string instead of index

base case(s)
both pattern and input are empty # True
one (pattern or input) are empty  

return booleon if input is a match of the pattern

"""
def word_pattern_match(pattern: str, input_str: str, pattern_idx: int = 0, input_idx: int = 0, char_to_word: dict = None): # dict = {}
    # Initialize the dictionary on the first call
    if char_to_word is None:
        char_to_word = {}

# base cases
    # If both pattern and input are fully processed, return True- meaning:
    # pattern_idx == len(pattern): processed all characters in pattern
    # input_idx == len(input_str): processed all characters in input_str

    if pattern_idx == len(pattern) and input_idx == len(input_str):
        return True
    
    # If one is empty but not the other, return False; checks if either the pattern or input_str has been fully processed, but not both. If I reach the end of one string while the other still has characters left, it means no valid split can be made, so return False.

    if pattern_idx == len(pattern) or input_idx == len(input_str):
        return False

    # Get the current character in the pattern
    char = pattern[pattern_idx]
    
    # Try to assign part of the string of input to this character
    """
First get the current character from the pattern, then try different substrings of input_str that start at input_idx.
end_idx goes from input_idx + 1 to len(input_str) + 1, meaning that it tries every possible substring from the current position input_idx to the end of input_str.

extracts a substring starting at input_idx and ending at end_idx. if input_str is 'redbluegreenbluered' and input_idx is 0, the first substring tried will be 'r', then 're', then 'red' etc
    """
    for end_idx in range(input_idx + 1, len(input_str) + 1):
        word = input_str[input_idx:end_idx]

# if len(input string) < len(pattern string) return 

# if the char (in pattern) has already been mapped to a word (already in the dictionary) check if the substring (word) matches the mapped word. If it does, call the function to process the next character in the pattern and continue splitting the remaining part of input_str 
# pattern_idx + 1:  move to the next character in the pattern.
# end_idx becomes the new input_idx, as the substring as been processed from input_idx to end_idx.
    
        # If the character has been mapped before
        if char in char_to_word:
            # Check if the dictionary entry matches the current substring
            if char_to_word[char] == word:
                # try to match the remaining pattern and input
                if word_pattern_match(pattern, input_str, pattern_idx + 1, end_idx, char_to_word):
                    return True
# If the character in the pattern hasn't been mapped yet (not in the dictionary), try mapping it to the current substring word. but first check if this word has already been mapped to a different character. If not, add to the dict and then try to match the remaining pattern and input_str.
# If there is a match return True. Otherwise go back by removing the newly added key value pair and try the next possible substring

        # If the character is not yet in the dictionary, ensure the word isn't used already
        elif word not in char_to_word.values():
            # Add the new key value pair and continue recursion
            char_to_word[char] = word
            if word_pattern_match(pattern, input_str, pattern_idx + 1, end_idx, char_to_word):
                return True
            # remove the key value pair
            del char_to_word[char]

    # If no valid matchh was found, return False
    return False

print(word_pattern_match('abcba', 'redbluegreenbluered'))  # True
print(word_pattern_match('aba', 'xxyyyxx'))  # True
print(word_pattern_match('abba', 'redbluegreenred'))  # False


# consider try again using slicing [:] 