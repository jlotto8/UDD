# What are all of the words that contain the word CAT and are exactly 5 letters long?
# What are all of the words that contain the word CAT and are exactly 5 letters long?

fn = 'sowpods.txt'
fh = open(fn)

for line in fh:
    line = line.strip()
    if 'CAT' in line and len(line) == 5:
            print(line)