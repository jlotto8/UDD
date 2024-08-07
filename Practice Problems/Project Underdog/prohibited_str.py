"""
Interview question: prohibited strings

Goal: solve this problem in < 60 minutes.

Write a function that takes two arguments, a list of prohibited strings and a username, and returns a boolean of whether or not the username contains any of the prohibited strings.

Some important details:

- The list of prohibited words will provide words in some casing, and we want to be case-insensitive in our checks. For example, if “darn” is a prohibited word, “darn”, “DARN” and “DaRn” are all prohibited.
- Sometimes people like to make usernames that substitute numbers for letters, to try to get around a prohibited word list. We also want to make those substitutions prohibited. The specific letter substitutions we need to check are:
    - A becomes 4
    - E becomes 3
    - I becomes 1
    - O becomes 0
    - For example, if “darn” is a prohibited word, “d4rn” is also a prohibited word. If “darn” and “heck” are prohibited words, the username “D4RN_y0u_T0_h3ck” contains prohibited words.


pseudocode

create a function that has input of a list of strings, and a username
create a dict to store all of the letter and number subsitutions
separate function  to convert the input username to  all lowercase letters, all letters, no numbers

"""

# def simplest_form(username):

#     # subsitutions_dict = {'A': '4', 'E': '3', 'I': '1', 'O': '0'} 
# # int changed to str for the replace method to work 
#     username= username.lower()
#     new_username = []
#     for char in username:
#         if char in substitutions_dict:
#             new_username.append(substitutions_dict[char])
#         else:
#             new_username.append(char)
#     new_username = ''.join(new_username)
#     return new_username
# print(simplest_form('d4rn'))

# Substitution Dictionary
# substitutions_dict = {
#     'a': '4', '4': 'a',
#     'e': '3', '3': 'e',
#     'i': '1', '1': 'i',
#     'o': '0', '0': 'o'
# }
substitutions_dict = {'4': 'a', '3': 'e', '1': 'i', '0': 'o'}
# Function to Normalize Username
def normalize_username(username):
    username = username.lower() # consider a different string method like replace; chain the . methods
    normalized_username = []

    for char in username:
        if char in substitutions_dict:
            normalized_username.append(substitutions_dict[char])
        else:
            normalized_username.append(char)
    return ''.join(normalized_username)
print(normalize_username('d4rn'))

# Function to Check for Prohibited Words
def is_prohibited(prohibited_words, username):
    normalized_username = normalize_username(username)
    for word in prohibited_words:
        if word.lower() in normalized_username:
            return True
    return False

# Example Usage
prohibited_words = ['darn', 'heck']
username = 'D4RN_y0u_T0_h3ck' # consider adding more username tests; loop through; print username and boolean true or false
print(is_prohibited(prohibited_words, username))  # Expected output: True

# test with basic inputs 
# sys 
