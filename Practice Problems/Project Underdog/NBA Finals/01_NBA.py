# Write a function that takes as an argument a year and returns the winner of the NBA finals that year.

# using with open automatically closes the file after the block of code runs; row is an array, each element is a column

"""
create a function that takes year as the parameter
loop through each row of the csv file
    if the parameter year is the same as row[0]/ the first element in the row:
        create a variable winner that is the second element in the row
return the second element in the row; row[1]
"""

import csv

def nba_winner_by_year(year):
    with open('nba_finals.csv', newline='') as csvfile:
        nba_file_reader = csv.reader(csvfile, delimiter=',')

        for row in nba_file_reader:
            if year == row[0]:
                winner = row[1]
        
        return winner

print(nba_winner_by_year('2016'))