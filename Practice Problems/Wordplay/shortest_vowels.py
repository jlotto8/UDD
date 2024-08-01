# What is the shortest word that contains all 5 vowels? 

fn = 'sowpods.txt'
fh = open(fn)

shortest = 150
shortest_word = 0
for line in fh:
    line = line.strip()
    if 'A' in line and 'E' in line and 'I' in line and 'O' in line and 'U' in line:
        if shortest > len(line):
            shortest = len(line)
            shortest_word = line
print(shortest_word)