
# [ ] Print out all of the #1 songs and the artists who made them. If a song was #1 for more than one week, only print it once. Example output:
#     These were the number one songs of 2000:
#     "Try Again" - Aaliyah
#     "Say My Name" - Destiny's Child
#     "What A Girl Wants" - Christina Aguilera
#     "Maria Maria" - Santana Featuring The Product G&B
#     "Smooth" - Santana Featuring Rob Thomas
#     "Independent Women Part I" - Destiny's Child

"""
rank,song,artist,last-week,peak-rank,weeks-on-board,date
1,Independent Women Part I,Destiny's Child,1,1,15,2000-12-30

go through each row in the file
look at the #1 songs- peak-rank; keep track of all #1 songs starting at the beginning of the iteration
when the song is #1, note the artist and song title

all the numbers #1x will go in a set, as tuples
song name, artist in a tuple
Mike
"""

import csv
with open('billboard100_2000.csv', newline='') as csvfile: 
    billboard_file_reader = csv.DictReader(csvfile, delimiter=',')

    number_ones = set()

    for row in billboard_file_reader:
        if row['peak-rank'] == '1': # is 1 an int or string? cast it to int?
            number_ones.add((row['song'], row['artist'],)) # is this syntax right?
# print(number_ones)

    for song, artist in number_ones:
        print(f'These were the number one songs of 2000: "{song}" - {artist}')



# item potency; use comments for blockers/type errors
# defensive coding upcoming