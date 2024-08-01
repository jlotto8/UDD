# What country names are > 50% vowels?

"""
find len(country name)
number of vowels in each country
create a list of vowels
accumulator

if letter is in list of vowels
    increment the accumulator

if number > len/2
    add then to a list
"""

fn = 'countries.txt'
# fn = 'test_countries.txt'
fh = open(fn)

vowels = ['A','a','E','e','I','i','O','o','U','u']
more_than_50 = []
# v = 0

for line in fh:
    line = line.strip()
    l = len(line)

    v = 0
    for char in line:
        if char in vowels:
            # print(char, 'is a vowel')
            v += 1
    # print(v)

    if v > l/2: # verify >= vs > 'off by one error';  check python docs for '/' '//' -> rounds down    
        more_than_50.append(line)
print(more_than_50)
