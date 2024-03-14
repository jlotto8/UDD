# What is the distribution of ratings? (How many are PG, PG-13, R, etc.?)
# 
"""
create a dictionary
loop through the file
if rating is in the dictionary, increment the count
if it is not in the dictionary, set the count 1
"""  
import csv
with open('top_movies.csv', newline='') as csvfile: 
    movie_file_reader = csv.DictReader(csvfile, delimiter=',')

    ratings_dict = dict()

    for row in movie_file_reader:
        if row['Rating'] in ratings_dict:
            ratings_dict[row['Rating']] += 1
        else:
            ratings_dict[row['Rating']] = 1
print(ratings_dict)


# with open()- look up- when file closes