# What is the shortest country name? Make sure your solution can handle ties.

fn = 'countries.txt'
fh = open(fn)

m = 200000
shortest = []

for line in fh:
    line = line.strip()
    if len(line) < m: # changed <= to < 
        m = len(line)
        shortest = [line] # clears/resets the list add only the most recent shortest
    elif len(line) <= m: #elif  to account for ties
        shortest.append(line)
print(shortest)

