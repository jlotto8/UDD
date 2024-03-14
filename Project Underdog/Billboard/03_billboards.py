# What artist had the most songs chart in 2000, and what were those songs?

"""
create a dictionary with the artist name as key, the value as a set of songs

loop through the dictionary
find the longest set
print the key and value/set

rank,song,artist,last-week,peak-rank,weeks-on-board,date
1,Independent Women Part I,Destiny's Child,1,1,15,2000-12-30
"""

import csv
with open('billboard100_2000.csv', newline='') as csvfile: 
    billboard_file_reader = csv.DictReader(csvfile, delimiter=',')

    most_songs_by_artist = dict()

    for row in billboard_file_reader:
        if row['artist'] in most_songs_by_artist:
            # print(most_songs_by_artist[row['artist']])
            most_songs_by_artist[row['artist']].add(row['song'])
        else:
            most_songs_by_artist[row['artist']] = {row['song']} 
# print(most_songs_by_artist)

    # DS literals;  set([]) set(())
    # no-op 

    longest_set = float('-inf')
    artist = []
    songs = []
    
    for key,value in most_songs_by_artist.items():
        if len(value) > longest_set:
            longest_set = len(value)
            artist = key
            songs = value
    print(longest_set)
    print(artist)
    print(songs)

# homework - account for ties