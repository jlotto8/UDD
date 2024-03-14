# What is the highest grossing movie from Universal Pictures, domestically?

"""
create a variable of highest grossing movie, list

current_highest_sales = float(-'inf)
current_title = ""

loop through csv with a for loop
check if the distrubtor is Universal
if it is, check the US sales
if the sales is higher than the current_highest_sales
reset the variable current_highest_sales = that sale price
current_title will equal the title key

"""

import csv
with open('top_movies.csv', newline='') as csvfile:
    movie_file_dict = csv.DictReader(csvfile, delimiter=',')

    highest_running_sale = 0
    running_title = ""

    for row in movie_file_dict:
        if row['Distributor'] == 'Universal Pictures':
            # print(type(highest_running_sale))
            if int(row['US Sales']) > highest_running_sale:
                highest_running_sale = int(row['US Sales'])
                running_title = row['Title']
print(running_title)

