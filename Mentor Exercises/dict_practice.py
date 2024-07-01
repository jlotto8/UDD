# what team has won the NBA finals the greatest number of times?
# which team has the largest number of distinct MVPs? (assuming the MVP is the MVP of the winning team)

# def dict_of_letters(word):
#     letter_dict = {}
#     for char in word:
#         if char in letter_dict:
#             letter_dict[char] +=1
#         else:
#             letter_dict[char] = 1
#     return(letter_dict)
# print(dict_of_letters('banana'))

import csv

with open('../Practice Problems/Project Underdog/NBA Finals/nba_finals.csv', newline='') as csvfile: 
    nba_file_dict = csv.DictReader(csvfile, delimiter=',')

winner_counts = dict()

for row in nba_file_dict:
    if row['Winner'] in winner_counts:
        winner_counts[row['Winner']] += 1 
    else:
        winner_counts[row['Winner']] = 1

most_often_winner = max(winner_counts)

