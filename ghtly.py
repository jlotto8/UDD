# Create and print an array containing all of the words that end in "GHTLY"

fn = 'sowpods.txt'
fh = open(fn)

ghtly = []
for line in fh:
    line = line.strip()
    if line.endswith('GHTLY'):
        ghtly.append(line)
print(ghtly)

