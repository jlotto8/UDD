# What are all of the words that have all 5 vowels, in alphabetical order?
"""
vowels = [a,e,i,o,u]
vowels_in_order = create a list to hold the words that contain all vowels in order
loop through each word in the file- ? for line in fh? or for i in range fh?
find and compare the indexes of the vowels- so that the index of each vowel is lower than the index of the next vowel
if the word contains all the vowels:
    use find() which returns the first occurance, or lowest index of a character in a string, if not in string, returns -1; find the first occurance of 'A', then find the first occurance of 'E'
    put all the positions in a list
    if positions list == ascending order
    add word to vowels_in_order list
return vowels_in_order
    """

# fn = 'sowpods.txt'
# fh = open(fn)

# vowel_list = ['A','E','I','O','U']
# vowels_in_order = []
# for line in fh:
#     line = line.strip()
#     if 'A' in line and 'E' in line and 'I' in line and 'O' in line and 'U' in line:
#         positions = []
#         for vowel in vowel_list:
#             positions.append(line.find(vowel))
#         if positions == sorted(positions):
#             vowels_in_order.append(line)
# print(vowels_in_order)


"""
12/7/23 attempt #2 to solve using no more than O(n) time complexity
vowel_list = ['A'....] list of vowels
vowel_dict = {'A': 0, 'E':0....} - dictionary to store the position of each vowel key = vowel, value = position
words = [] - list to store lines/words where vowels are present and in order

Set all of the positions of all vowels in the dictionrary to -1 so that if the letter is not found, it flags to false when I need to break out of the loop
Iterate through each line in the file
for line in fh:
    line = line.strip()

    Iterate through each letter in the line with enumerate to access element and index
    for i, char in enumerate(line):
        Check if the character is a vowel
        if char in vowel_dict:
            # Update the position of the vowel
            vowel_dict[char] = i

    # Check if all vowels are present and in order
    vowels_present = True
    for vowel in vowel_list:
        if vowel_dict[vowel] == -1:
            vowels_present = False
            break

    # Check if vowels are in order
    if vowels_present:
        for i in range(len(vowel_list) - 1):
            if vowel_dict[vowel_list[i]] > vowel_dict[vowel_list[i + 1]]:
                vowels_present = False
                break

    # Append the line to the result list if all vowels are present and in order
    if vowels_present:
        words.append(line)

# Print the result list
print(words)
"""
# fn = 'sowpods.txt'
# fh = open(fn)

# vowel_list = ['A','E','I','O','U']
# vowels_dict = {'A': -1,'E': -1,'I': -1,'O': -1,'U': -1}
# words = []

# for line in fh:
#     line = line.strip()
#     for i, char in enumerate(line):
#         if char in vowel_dict:
#             vowel_dict[char] = i
    
#     vowels_present = True
#     for vowel in vowel_list:
#         if vowel_dict[vowel] == -1:
#             vowels_present = False
#             break
#     if vowels_present:
#         for i in range(len(vowel_list) - 1):
#             if vowel_dict[vowel_list[i]] > vowel_dict[vowel_list[i + 1]]:
#                 vowels_present = False
#                 break
#     if vowels_present:
#         words.append(line)
# print(words)
  
# fn = 'sowpods.txt'
# fh = open(fn)

# vowel_list = ['A', 'E', 'I', 'O', 'U']
# # Manually create a dictionary to store the position of each vowel with initial values
# # inf represents an infinite upper bound value, and ensures that the actual index/position found will be less than infinity
# vowels_dict = {'A': float('inf'), 'E': float('inf'), 'I': float('inf'), 'O': float('inf'), 'U': float('inf')}
# # List to store lines where all vowels are present and in order
# words = []
# for line in fh:
#     line = line.strip()
#     # Check if all vowels are present 
#     vowels_present = True
#     for vowel in vowel_list:
#         if vowel not in line: # only looking for the words that contain all vowels
#             vowels_present = False 
#             break
#         else:
#             index = line.find(vowel) 
#             if index > vowels_dict[vowel]: # checks if the current index is greater than the stored index in the dictionary for the same vowel. If it is, it means the vowels are not in order, and it sets vowels_present to False and breaks out of the loop.
#                 vowels_present = False
#                 break
#             vowels_dict[vowel] = index #If the index is smaller or equal, it updates the stored index in the dictionary: vowels_dict[vowel] = index.

#     # Append the line to the result list if all vowels are present and in order
#     if vowels_present:
#         words.append(line)

# # Print the result list
# print(words)
"""
Checks if the current character matches the vowel at the current position (i) in vowel_list.
If so, increments i.
If i reaches the length of vowel_list, the word has all vowels in order, so it's added to the words list, and the inner loop is terminated.
"""

# fn = 'sowpods.txt'
# fh = open(fn)

# vowel_list = ['A', 'E', 'I', 'O', 'U']
# words = []
# i = 0

# for line in fh:
#     line = line.strip()
#     for i in line:
#         if i <len(vowel_list) and line[i] == vowel_list[i]:
#             i += 1
#         if i == len(vowel_list):
#             words.append(line.strip())
#             break
#     elif line[i] in vowel_list:
#         i = 0
# print(words)

# fn = 'sowpods.txt'
# fh = open(fn)
# vowel_list = ['A', 'E', 'I', 'O', 'U'] # list of vowels
# # dict to store the position of each vowel with initial values inf represents an infinite upper bound value, and ensures that the actual index found will be < infinity
# vowels_dict = {'A': float('inf'), 'E': float('inf'), 'I': float('inf'), 'O': float('inf'), 'U': float('inf')}
# # List to store lines/words where all vowels are present and in order
# words = []
# for line in fh:
#     line = line.strip()
#     vowels_present = True 
#     for vowel in vowel_list: 
#         if vowel not in line: # Check if all vowels are present,only looking for words with all vowels
#             vowels_present = False 
#             break
#         else:
#             index = line.find(vowel) 
#             if index > vowels_dict[vowel]: # checks if the current index > the stored index in the dict for the same vowel. If yes, the vowels not in order, vowels_present = False and breaks out
#                 vowels_present = False
#                 break
#             vowels_dict[vowel] = index #If the index <=, it updates the stored index in the dict
#     if vowels_present:
#         words.append(line) # append the line to the result liine
# print(words)

# fn = 'sowpods.txt'
# fh = open(fn)

# vowel_list = ['A', 'E', 'I', 'O', 'U']
# words = []
# for line in fh:
#     line = line.strip()
#     i = 0
#     for char in line:
#         if i < len(vowel_list) and char == vowel_list[i]:
#             i += 1
#             if i == len(vowel_list):
#                 words.append(line)
# print(words)

# fn = 'sowpods.txt'
# fh = open(fn)

# vowel_list = ['A', 'E', 'I', 'O', 'U']
# words = []
# for line in fh:
#     line = line.strip()
#     i = 0
#     for char in line:
#         if i < len(vowel_list) and char == vowel_list[i]:
#             i += 1
#             if i == len(vowel_list):
#                 words.append(line)
#                 # break
#         # elif char in vowel_list:
#         #     # If a vowel is encountered out of order, reset the position
#         #     i = 0
# print(words)


fn = 'sowpods.txt'
fh = open(fn)

vowel_list = ['A', 'E', 'I', 'O', 'U']
words = []

for line in fh:
    line = line.strip()
    i = 0 # keeps track of the index in the vowel list
    valid_word = True

    for char in line:
        if i < len(vowel_list) and char == vowel_list[i]: # if the current character matches the expected vowel in the order. If yes, it increments i
            i += 1
        elif char in vowel_list:
            # Additional vowel found in a position other than the expected order
            valid_word = False
            break

    if i == len(vowel_list) and valid_word:
        words.append(line)

print(words)