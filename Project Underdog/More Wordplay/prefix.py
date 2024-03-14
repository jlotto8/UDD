# Write a function that takes a string prefix as an argument and returns an array of all of the words that start with that prefix (the prefix has to be at the beginning of the word).

def find_prefix(prefix):

    file_name = '../../Wordplay/sowpods.txt'
    file_handle = open(file_name)

    results = []

    results = [word.strip() for word in file_handle if word.startswith(prefix)]
    # results = [word.strip() for word in file_handle if substring in word]
    # for word in file_handle:
    #     word = word.strip()

    #     if substring in word:
    #         results.append(word)
    return results

print(find_prefix('INTRO'))