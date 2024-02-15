import timeit
# There is at least one baby name from the top 40 baby names for 2020 that, when spelled backwards, is a valid Scrabble word. Find and print all such names.
# Solve this two ways: first with an array to hold the Scrabble words, and then with a dictionary (or set) to hold the Scrabble words. Use timer functions to measure how long it takes to complete this work under each implementation. Why is the time different?
 
# def find_babynames_in_scrabble():
#     scrabble_file = '../../Wordplay/sowpods.txt'
#     scrabble_handle = open(scrabble_file)

#     list_of_scrabble_words = set()
#     list_of_names = []

#     for word in scrabble_handle:
#         word = word.strip()
#         list_of_scrabble_words.add(word)

#     baby_name_file = 'babynames_2020.txt'
#     baby_name_handle = open(baby_name_file)
#     for line in baby_name_handle:
#         name = line.strip()
#         reversed_name = name[::-1]
#         reversed_name = reversed_name.upper()
#         # for word in scrabble_handle: # 'Henry' not included in output, file has to be  opened with new handle 
#         #     word = word.strip()
#         if reversed_name in list_of_scrabble_words:
#             list_of_names.append(name)
#     return list_of_names

# print(find_babynames_in_scrabble())
# print(timeit.default_timer())

def find_babynames_in_scrabble():
    scrabble_file = '../../Wordplay/sowpods.txt'
    scrabble_handle = open(scrabble_file)

    list_of_scrabble_words = [] 
    for word in scrabble_handle:
        word = word.strip()
        list_of_scrabble_words.append(word)

    baby_name_file = 'babynames_2020.txt'

    list_of_names = []

    baby_name_handle = open(baby_name_file)
    for line in baby_name_handle:
        name = line.strip()
        reversed_name = name[::-1]
        reversed_name = reversed_name.upper()
        # for word in scrabble_handle: # 'Henry' not included in output, file has to be  opened with new handle 
        #     word = word.strip()
        if reversed_name in list_of_scrabble_words:
            list_of_names.append(name)
    return list_of_names

print(find_babynames_in_scrabble())
print(timeit.default_timer())