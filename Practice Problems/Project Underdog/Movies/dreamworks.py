# What movies on this list were distributed by DreamWorks?
from movies import movies_data

# print(movies_data)

"""
create a list to hold results
loop through list of dict
if 'distributor' == 'Dreamworks'
    add to list
print the list of results
"""

movies_by_dreamworks = []
for movie in movies_data:
    if movie['Distributor'] == 'DreamWorks Distribution':
        # print(movie)
        movies_by_dreamworks.append(movie['Title'])
print(movies_by_dreamworks)

# def find_distributer(distributer, movie_list):
#     distributer_movies = []
#     for movie in movie_list:
