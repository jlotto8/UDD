# How many words contain the substring "TYPE”?

fn = 'sowpods.txt'
fh = open(fn)

type_count = 0
for line in fh:
    line = line.strip()
    if 'TYPE' in line:
        type_count += 1
print(type_count)
