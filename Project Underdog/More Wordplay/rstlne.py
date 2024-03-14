import timeit

# What are all of the words that can be made from only the letters in “RSTLNE”? Not all of those letters need to be used, and letters can be repeated.

"""
create a list to hold results
create a list of the letters to be used rstlne

loop through each word in the file
    for in char in line
         if char in 'rstlne':
            add to result list
"""
file_name = '../../Wordplay/sowpods.txt'
file_handle = open(file_name)

results = []
letters = set(['R','S','T','L','N','E']) 

sample_word = 'SAMPLE'
for line in file_handle:
    line = line.strip()

    invalid = False
    for char in line:
        if char not in letters: # if letters = set,  will be O(1)
            invalid = True
            break
            
    if invalid == False:
        results.append(line)
        print(len(line))

print(results)


