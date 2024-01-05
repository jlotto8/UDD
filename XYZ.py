fn = 'sowpods.txt'
fh = open(fn)
for line in fh:
    if 'X' in line and 'Y'in line and 'Z' in line:
        line = line.strip()
        print(line)
