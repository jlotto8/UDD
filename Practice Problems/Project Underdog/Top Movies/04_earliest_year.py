# What is the earliest year on this list, and what were the films from that year?

"""
Create a list to store the results, titles
create a variable = inf
loop through the file
cast the year to an int
check if the year is less than inf
if it is, reset the variable name to that year
list= that title name
check if year is the same as the next year
 append the titles to the list
"""

import csv
with open('top_movies.csv', newline='') as csvfile:
    movie_file_reader = csv.DictReader(csvfile, delimiter=',')
 
    title_results = []

    earliest_running_year = float('inf')

    for row in movie_file_reader:
        if int(row['Release Date']) < earliest_running_year:
            earliest_running_year = int(row['Release Date'])
            title_results = [row['Title']]

        elif int(row['Release Date']) == earliest_running_year:
            title_results.append(row['Title'])
print(title_results, earliest_running_year)

