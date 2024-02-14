# What countries use only one vowel in their name (the vowel can be used multiple times)
# - For example, if the word “BEEKEEPER” were a country, it would be an answer, because it only uses “E”.

"""
loop through each line
create count to  keep track of vowels
    loop through each character in each line
    if count == 1
    return those lines
"""

vowels = ['A','a','E','e','I','i','O','o','U','u']

fn = 'countries.txt'
fh = open(fn)

one_vowel = []

for line in fh:
    line = line.strip()

    seen = set()
    for char in line:
        if char in vowels:
            seen.add(char.upper())

    if len(seen) == 1:
        one_vowel.append(line)

print(one_vowel)

# every line is either a conditional or executing mult times  
# inside loop- what is it iterating over 



