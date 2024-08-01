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
from collections import Counter
import csv
with open('billboard100_2000.csv', newline='') as csvfile: 
    billboard_file_reader = csv.DictReader(csvfile, delimiter=',')

    most_charted = Counter()

    for row in billboard_file_reader:
        song_artist_tuple = (row['song'], row['artist'],)
        # song_artist_tuple = (row['song'], row['artist'],) # why won't this work?
        # most_charted.update({song_artist_tuple:1})
        # most_charted.update(song_artist_tuple)
        # most_charted[song_artist_tuple] += 1
    # print(most_charted)
        # if (row['song'],row['artist']) in most_charted:
        most_charted.update((row['song'],row['artist'],)) # use join to convert tuple 
    print(most_charted)
    # most_charted = dict()

    # for row in billboard_file_reader:

    #     if (row['song'],row['artist']) in most_charted:
    #         most_charted[(row['song'],row['artist'],)] += 1
    #     else:
    #         most_charted[(row['song'],row['artist'],)] = 1
    # # print(most_charted)

    # def find_songs_most_charted(song_data):

    #     song_count = float('-inf')
    #     songs = ()
    #     artists = ()

    #     for key_tuples, value in most_charted.items():
    #         if value > song_count:
    #             song_count = value
    #             songs = (key_tuples[0])
    #             artists = (key_tuples[1])
    #         elif song_count == value:
    #             songs.add(key_tuples[0])
    #             artists.add(key_tuples[1])
    #     return songs

    # print(find_songs_most_charted(song_data = most_charted))



