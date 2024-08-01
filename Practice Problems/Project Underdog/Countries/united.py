# What are all of the countries that have “United” in the name?

fn = 'countries.txt'
fh = open(fn)

united = []

for line in fh:
    line = line.strip()
    if 'United' in line:
        united.append(line)

print(united)