# What movies on this list were distributed by DreamWorks?

"""
create a list to hold the results

loop through the csv, for loop 
check if the key distributer is DreamWorks
if it is, add the title to the results list
"""
import csv
with open('top_movies.csv', newline='') as csvfile: 
    movie_file_dict = csv.DictReader(csvfile, delimiter=',')

    movie_results = []

    for row in movie_file_dict:
        if row['Distributor'] == 'DreamWorks':
            movie_results.append(row['Title'])
    print(movie_results)


# when does file close after using with open()