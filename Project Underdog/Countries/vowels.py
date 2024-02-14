# What countries both begin and end with a vowel?

fn = 'countries.txt'
fh = open(fn)

vowels = []
tuple_vowels = ('A','E','I','O','U')
lower = ('a','e','i','o','u')

for line in fh:
    line = line.strip()
    if line.startswith(tuple_vowels) and line.endswith(lower):
        vowels.append(line)
print(vowels)

# consider trying again, check each word in the country