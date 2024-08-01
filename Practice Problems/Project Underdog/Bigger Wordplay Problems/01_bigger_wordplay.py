# What is the longest word where no letter is used more than once?
"""
longest word = float (-inf)
result_word = word

loop through each word
    set
    duplicate_letter = False
    loop through letter
        check if the letter is in the set
            if not add each letter to the set
            if yes- letter already in the set:
                duplicate_letter = True
                break
    if flag == False 
        check length of each word
        if it's > longest word
            reset the variable longest word to that len(word)
            result_word = word
return results
"""

file_name = '../../Wordplay/sowpods.txt'
file_handle = open(file_name)

longest_word = float('-inf')
result_word = ""

for line in file_handle:
    line = line.strip()
    seen_letter = set()
    duplicate_letter = False

    for letter in line:
        letter = letter.strip()
        if letter not in seen_letter: # flip conditional 
            seen_letter.add(letter)
            # print(seen_letter)
        else:
            duplicate_letter = True
            break
    
    if duplicate_letter == False: # if not duplicate letter
        if len(line) > longest_word:
            longest_word = len(line)
            result_word = line
print(result_word, longest_word)


# pseudocode helped the code; 