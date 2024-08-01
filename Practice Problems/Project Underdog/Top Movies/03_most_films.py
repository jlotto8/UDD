# What distributor has the most films on this list?
from collections import Counter
"""
create a dict/counter
loop through the file
add each distributor to the dict, and increment

to find the max:
set a variable to -inf
loop through the counter dict that i created
compare each value to -inf
if the value is higher, reset the variable name to that value
print the variable at the end
"""

import csv
with open('top_movies.csv', newline='') as csvfile:
    movie_file_reader = csv.DictReader(csvfile, delimiter=',')

    distributor_count = Counter()

    for row in movie_file_reader:
        if row['Distributor']:
            distributor_count.update([row['Distributor']])
print(distributor_count.most_common(1)[0][0])

# careful with variable names, file names; counter is a subclass of dict
