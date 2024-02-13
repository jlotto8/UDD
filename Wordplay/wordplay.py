# starts with q ends with z <6 chars long
# words with 1 vowel
# words with 'U' but no other vowels


"""
[ ] What are all of the words containing UU?
[ ] What are all of the words containing an X and a Y and a Z?
[ ] What are all of the words containing a Q but not a U?
[ ] What are all of the words that contain the word CAT and are exactly 5 letters long?
[ ] What are all of the words that have no E or A and are at least 15 letters long?
[ ] What are all of the words that have a B and an X and are less than 5 letters long?
[ ] What are all of the words that both start and end with a Y?
[ ] What are all of the words with no vowel and not even a Y?
[ ] What are all of the words that have all 5 vowels, in any order?
[ ] What are all of the words that have all 5 vowels, in alphabetical order?

Setting up storage to use during a for loop, including counters and arrays

[ ] How many words contain the substring "TYPE”?
[ ] Create and print an array containing all of the words that end in "GHTLY"
[ ] What is the shortest word that contains all 5 vowels?
[ ] What is the longest word that contains no vowels?
[ ] Which of the letters Q, X, and Z is the least common?
[ ] What is the longest palindrome?
[ ] What are all of the letters that never appear consecutively in an English word? For example, we know that “U” isn’t an answer, because of the word VACUUM, and we know that “A” isn’t an answer, because of “AARDVARK”, but which letters never appear consecutively?
"""
fn = 'sowpods.txt'
fh = open(fn)


# What are all of the words containing UU?
# UU = []
# for line in fh:
#     line.strip()
#     if 'UU' in line:
#         UU.append(line.strip())
# print(UU)

# What are all of the words containing an X and a Y and a Z?
# xy = []
# for line in fh:
#     if 'X' in line and 'Y'in line and 'Z' in line:
#         # line = line.strip()
#         print(line)
#         xy.append(line)
# print(xy) 
# My syntax was wrong, which is why it wasn't working previoulsy
# Q: why didn't I have to strip anything to just print? but adding to a list I do? 

# What are all of the words containing a Q but not a U?
# q = []
# for line in fh:
#     if 'Q' in line and not 'U' in line:
#         print(line)
#         q.append(line.strip())
# # print(q)

# # Q: Why doesn't this code below work?
# for line in fh:
#     if 'Q' in line:
#         q.append(line)
# for word in q:
#     if "U" in word:
#         q.remove(word)
# print(q)

# What are all of the words that contain the word CAT and are exactly 5 letters long?
# cat = []
# for line in fh:
#     if 'CAT' in line:
#         if len(line) == 5:
#             print(line)
#             cat.append(line.strip())

# for line in fh:
#     if 'CAT' in line and len(line) == 5:
#         print(line)
# Is one of these solutions better than the other? 

# What are all of the words that have no E or A and are at least 15 letters long?
# no_a_e = []
# for line in fh:
#     if 'E' not in line and 'A' not in line:
#         if len(line) >= 15:
#             print(line)
#             no_a_e.append(line.strip())
# print(no_a_e)

# What are all of the words that have a B and an X and are less than 5 letters long?
# for line in fh:
#     if 'B' in line and 'X' in line and len(line) < 5:
#         print(line)
# How do I know if this is correct? 

# What are all of the words that both start and end with a Y?
# for line in fh:
#     line = line.strip() 
#     if line.startswith('Y'):
#         # print(line)
#         if line.endswith('Y'):
#             print(line)
# this only works after line 90 was added, why?  

# What are all of the words with no vowel and not even a Y?
# for line in fh:
#     if not 'A' in line and not 'E' in line and not 'I' in line and not 'O' in line and not 'U' in line and not 'Y' in line:
#         print(line)
# Is there a better way to write this? It seems clumsy or something?

# What are all of the words that have all 5 vowels, in any order?
# vowels = []
# for line in fh:
#     if 'A' in line and 'E' in line and 'I' in line and 'O' in line and 'U' in line:
#         print(line)
#         vowels.append(line.strip())
# print(vowels)

# What are all of the words that have all 5 vowels, in alphabetical order?

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

# this solution took me literal days of thinking about it 
# Try again with O(n)

# START HERE FOR REVIEW ON DEC 8TH


"""
Try again with one time through the words, and in O(n) 
"""
fn = 'sowpods.txt'
fh = open(fn)

vowel_list = ['A', 'E', 'I', 'O', 'U']
words = []
for line in fh:
    line = line.strip()
    i = 0
    for char in line:
        if i < len(vowel_list) and char == vowel_list[i]:
            i += 1
            if i == len(vowel_list):
                words.append(line)
                # break
        # elif char in vowel_list:
        #     # If a vowel is encountered out of order, reset the position
        #     i = 0
print(words)

# How many words contain the substring "TYPE”?
# type_count = 0
# for line in fh:
#     line = line.strip()
#     if 'TYPE' in line:
#         type_count += 1
# print(type_count)


# Create and print an array containing all of the words that end in "GHTLY"
# ghtly = []
# for line in fh:
#     line = line.strip()
#     if line.endswith('GHTLY'):
#         ghtly.append(line)
# print(ghtly)
# note- last 5 indexes

# ghtly = []
# for line in fh:
#     line = line.strip()
#     if line[-5:] == 'GHTLY':
#         ghtly.append(line)
# print(ghtly)


# What is the shortest word that contains all 5 vowels? 
# shortest_word = 0

# for line in fh:
#     line = line.strip()
#     if 'A' in line and 'E' in line and 'I' in line and 'O' in line and 'U' in line:
#         if shortest > len(line):
#             shortest = len(line)
#             # word += line
#             shortest_word = line
# print(shortest_word)

# What is the longest word that contains no vowels?
# longest = 0
# word = 0
# for line in fh:
#     line = line.strip()
#     if not 'A' in line and not 'E' in line and not 'I' in line and not 'O' in line and not 'U' in line:
#         if longest < len(line):
#             longest = len(line)
#             word = line
# print(word)

#Which of the letters Q, X, and Z is the least common?
# q = 0
# x = 0
# z = 0

# for line in fh:
#     line = line.strip()
#     if 'Q' in line:
#         q += 1
#     if 'X' in line:
#         x += 1
#     if 'Z' in line:
#         z += 1
# print(min(q,x,z))

# this gives me the number of words that is the highest out of each option(q,x,z) but not the variable name.   Do I need to loop through the 3 to find which letter? Or multiple comparison operators/booleans like if q >x etc?
# Or use a different data structure and logic completely like below *not my code**
# counts = {'Q': 0, 'X': 0, 'Z': 0}

# for line in fh:
#     line = line.strip()
#     for letter in counts:
#         if letter in line:
#             counts[letter] += 1
# least_common_letter = min(counts, key=counts.get)
# least_common_count = counts[least_common_letter]

# What is the longest palindrome?
# longest = 0
# word = ''
# for line in fh:
#     line = line.strip()
#     if line == line[::-1]:
#         if len(line) > longest:
#             longest = len(line)
#             word = line
# print(longest,word)
# Is there a way to do this using a more classic palindrome approach like:
# 
# for i in range(len(word)):
    # if word[i] != word[len(word)-i-1]:
        # continue
        # increment i, keep comparing until they meet in the middle, or cross over and continue until the end of the word
# I think I'm asking how to structure a loop using a text file, but going through each character as is possible using range


# What are all of the letters that never appear consecutively in an English word? For example, we know that “U” isn’t an answer, because of the word VACUUM, and we know that “A” isn’t an answer, because of “AARDVARK”, but which letters never appear consecutively?

# fn = 'sowpods.txt'
# fh = open(fn)

# alphabet = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
# consecutive_chars = set()
# for line in fh:
#     line = line.strip()
#     for i in range (len(line)-1):
#         if line[i] == line[i+1]:
#             consecutive_chars.add(line[i+1])
# result = alphabet  - consecutive_chars
# print(result)


# fn = 'sowpods.txt'
# fh = open(fn)

# alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# for line in fh:
#     line = line.strip()
#     for i in range(len(line) - 1):
#         if line[i] == line[i + 1]:
#             alphabet.discard(line[i])
# print(alphabet)