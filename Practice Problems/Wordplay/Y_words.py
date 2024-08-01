# What are all of the words that both start and end with a Y?

fn = 'sowpods.txt'
fh = open(fn)

for line in fh:
    line = line.strip() 
    if line.startswith('Y') and line.endswith('Y'):
      print(line)