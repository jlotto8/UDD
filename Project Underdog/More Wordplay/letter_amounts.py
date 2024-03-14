
# [ ] Let’s assign letters the following points:
#     - W = 12
#     - Z = 15
#     - E = -17
#     - All other letters = 1

# What are all of the words with at least 50 points?
"""

"""

file_name = '../../Wordplay/sowpods.txt'
file_handle = open(file_name)

letter_points = {
    'W': 12,
    'Z': 15,
    'E': -17
}

# if you know the key is present, you can use the key directly

default_point = 1
results = []

for word in file_handle:
    word = word.strip()

    total_points = 0

    for letter in word:
        total_points += letter_points.get(letter,default_point)
        # print(letter,total_points)

    if total_points >= 50:
        results.append(word)

print(results)
