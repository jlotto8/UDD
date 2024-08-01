# What is the longest word that contains no vowels?

fn = 'sowpods.txt'
fh = open(fn)

longest = 0
word = 0
for line in fh:
    line = line.strip()
    if not 'A' in line and not 'E' in line and not 'I' in line and not 'O' in line and not 'U' in line:
        if longest < len(line):
            longest = len(line)
            word = line
print(word)