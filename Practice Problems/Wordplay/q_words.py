# What are all of the words containing a Q but not a U?

fn = 'sowpods.txt'
fh = open(fn)

for line in fh:
    if 'Q' in line and not 'U' in line:
        print(line.strip())