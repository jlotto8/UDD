# What is the longest palindrome?

fn = 'sowpods.txt'
fh = open(fn)

longest = 0
word = ''
for line in fh:
    line = line.strip()
    if line == line[::-1]:
        if len(line) > longest:
            longest = len(line)
            word = line
print(longest,word)

    