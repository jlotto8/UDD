# What are all of the words that have all 5 vowels, in any order?

fn = 'sowpods.txt'
fh = open(fn)

for line in fh:
    line = line.strip()
    if 'A' in line and 'E' in line and 'I' in line and 'O' in line and 'U' in line:
        print(line)