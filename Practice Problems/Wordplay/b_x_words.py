# What are all of the words that have a B and an X and are less than 5 letters long?

fn = 'sowpods.txt'
fh = open(fn)

for line in fh:
    line = line.strip()
    if 'B' in line and 'X' in line and len(line) < 5:
        print(line)