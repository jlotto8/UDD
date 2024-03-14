# What are all of the words that start with “PRO”, end in “ING”, and are exactly 11 letters long?

"""
create a list to hold the results
loop through each word 
    use startswith() and endswith() to check the prefix and suffix of each word
    check the length of each word

    if all conditions are met
        add the word to the result list
"""

file_name = '../../Wordplay/sowpods.txt'
file_handle = open(file_name)

results = []

for line in file_handle:
    line = line.strip('[/')
    if line.startswith('PRO') and line.endswith('ING') and len(line) == 11:
        results.append(line)
print(results)