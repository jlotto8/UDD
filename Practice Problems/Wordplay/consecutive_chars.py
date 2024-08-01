# What are all of the letters that never appear consecutively in an English word? For example, we know that “U” isn’t an answer, because of the word VACUUM, and we know that “A” isn’t an answer, because of “AARDVARK”, but which letters never appear consecutively?

"""
alphabet_set = set of all the letters in the alphabet .upper()
consecutive_chars = set()- to store the letters that appear consecutively 
loop through each line
if line[i] == line[i+1]:
    add one of them to the set
return the intersection of both sets, or the difference between both sets
"""

fn = 'sowpods.txt'
fh = open(fn)

# alphabet = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
# consecutive_chars = set()
# for line in fh:
#     line = line.strip()
#     for i in range (len(line)-1):
#         if line[i] == line[i+1]:
#             consecutive_chars.add(line[i+1])
# result = alphabet  - consecutive_chars
# print(result)

fn = 'sowpods.txt'
fh = open(fn)

alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

for line in fh:
    line = line.strip()
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            alphabet.discard(line[i])
print(alphabet)

