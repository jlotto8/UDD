# What are all of the words with no vowel and not even a Y?

fn = 'sowpods.txt'
fh = open(fn)

for line in fh:
    line = line.strip()
    if not 'A' in line and not 'E' in line and not 'I' in line and not 'O' in line and not 'U' in line and not 'Y' in line:
        print(line)