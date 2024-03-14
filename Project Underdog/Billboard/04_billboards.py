# What song(s) were on the charts (anywhere on the charts) for the most weeks of 2000?

"""
use counter and dict() to solve this

create dictionary
add every song and artist as a tuple for the key, and count as the value

create a max value variable
create a list to hold the songs

loop through the dictionary
compare each value to the max
if the value > max
max = value
songs = key[1]

"""

import csv
with open('billboard100_2000.csv', newline='') as csvfile: 
    billboard_file_reader = csv.DictReader(csvfile, delimiter=',')

    