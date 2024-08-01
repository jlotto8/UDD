# What are all of the words that start with a Q, end with a Z, and are less than or equal to 6 letters long?
# word_list = "sowpods.txt"

# with open(word_list, 'r') as file: #represents the state of the program reading or writing
#     words = file.readlines() # reads file, saves to memory as a list 

# q_z_words = []
# for line in words:
#     line = line.strip()
#     if line.startswith('Q') and line.endswith('Z') and len(line) < 7:
#         q_z_words.append(line)
#         print(line)
# print(q_z_words)

# create and print words with U and no other vowel
word_list = 'sowpods.txt'

with open(word_list,'r') as file:
    words = file.readlines()

# u_words = []
# vowels = ['A','E','I','O']

# for line in words:
#     line = line.strip()
#     has_vowels = False

#     for letter in line:
#         if letter in vowels:
#             has_vowels = True
#             break
#     if 'U' in line and not has_vowels:
#         u_words.append(line)
# print(u_words)

word_list = 'sowpods.txt'

with open(word_list,'r') as file:
    words = file.readlines()

result = []
vowels = ['A','E','I','O','U','Y']
for line in words:
    line = line.strip()
    
    for letter in line:
        if letter in vowels:
            continue
        result.append(line)
    print(result)
    