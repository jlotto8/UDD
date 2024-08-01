# What are all of the words that have no E or A and are at least 15 letters long?

fn = 'sowpods.txt'
fh = open(fn)

for line in fh:
    line = line.strip()
    if 'E' not in line and 'A' not in line and len(line) >= 15:
            print(line)