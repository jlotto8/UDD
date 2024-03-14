# What song was the #1 song for the most weeks of 2000, who was the artist, and how many weeks was it at #1?

"""
rank,song,artist,last-week,peak-rank,weeks-on-board,date
1,Independent Women Part I,Destiny's Child,1,1,15,2000-12-30
1,Independent Women Part I,Destiny's Child,1,1,15,2000-12-23

1,x,x,x,x
1,x,x,x,x
1,x,x,x,x

1,Independent
1,

dictionary will hold the song title, artist as a tuple and then count how many times it is there each week
{(Survivor, Destiny's child: 2),
(Independent Woman, Destiny's child: 4)}
 
for key,value in dictionary.items()
look at every key and value
"""
# print(number_ones)
# .get()
"""
create a max variable
create a variable to hold the key - song, artist
loop through dictionary 
when the value is > max value
reset/rename the max variable to that value
print the key

"""
import csv
with open('billboard100_2000.csv', newline='') as csvfile: 
    billboard_file_reader = csv.DictReader(csvfile, delimiter=',')

    number_ones = dict()

    for row in billboard_file_reader:
        if row['rank'] == '1':
            if (row['song'], row['artist'],) in number_ones:
                number_ones[(row['song'],row['artist'],)] += 1
            else:
                number_ones [(row['song'],row['artist'],)] = 1

    highest_weeks = float('-inf')
    result = []

    for key_tuples, value in number_ones.items():
        if value > highest_weeks:
            highest_weeks = value
            result = [key_tuples]
        elif value == highest_weeks: 
            result.append(key_tuples)
print(result,highest_weeks)

# tuple unpacking
# create function for both parts of this problem
