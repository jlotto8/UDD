fn = 'sowpods.txt'
fh = open(fn)
for line in fh:
    line = line.strip()
    if 'UU' in line:
        print(line)