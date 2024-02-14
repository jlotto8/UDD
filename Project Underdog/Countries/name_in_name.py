# There is at least one country name that contains another country name. Find all of these cases.

"""
loop through each line
    loop through each word in each line; for word in line # generate pairs of country name
    if name has more than one word
        if name is in those words
"""

fn = 'countries.txt'
fh = open(fn)

names = []

for line in fh:
    line = line.strip()

    fh_two = open(fn)
    for line_B in fh_two:
        line_B = line_B.strip()
        # print(line, line_B)
        if line == line_B:
            continue
        elif line in line_B:
            names.append(line) # write a string 
            names.append(line_B)
print(names)


names = []
country_names = set()

for line in fh:
    line = line.strip()
    country_names.add(line)

    for word in country_names:
        if line == word:
            continue
        elif line in word or word in line:
            names.append(line)
            names.append(word)
print(names)


# case sensitivity
# find the words that appear in mult countries
# split lines
# 
# this solution is inefficient, better to read into memory once 