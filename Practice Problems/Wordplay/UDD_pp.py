# word_list = 'sowpods.txt'
# with open(word_list,'r') as file:
#     words = file.readlines()

# What are all of the words that start with a Q, end with a Z, and are less than or equal to 6 letters long?

fn = 'sowpods.txt'
fh = open(fn)

# create empty list to store the words

# for line in fh:
#     line = line.strip()
#     if line.startswith('Q') and line.endswith('Z') and len(line) < 7:
#         result.append(line)
# print(result)

# Create and print an array containing all of the words that have a U but no other vowel.
# result = []

# for line in fh:
#     line = line.strip()

#     has_vowel = False

#     for letter in line:
#         if letter in vowels:
#             has_vowel = True
#             break

#     if 'U' in line and not has_vowel:
#         result.append(line)
# print(result)

# Create and print an array containing all of the words that have only one kind of vowel in them.

result = []
vowels = ['A','E','I','O','U']
# current_vowel
for line in fh:
    line = line.strip()
    count = 0

    for vowel in vowels:
        if line.count(vowel):
            count += 1

    if count == 1:
        result.append(line)
print(result)


