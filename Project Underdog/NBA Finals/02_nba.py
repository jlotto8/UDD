# Write a function that takes as an argument a team name and returns an array of all of the years the team has won the NBA finals.

"""
create a function, team name as the parameter
create a list of years

loop through each row of the file
    if the team name is the same as the second item in the row:
        add the first item in the row to the list of years
return the list
"""
import csv

# def years_won(team):
#     with open('nba_finals.csv', newline='') as csvfile:
#         nba_file_reader = csv.reader(csvfile, delimiter=',')

#         list_of_years = []

#         for row in nba_file_reader:
#             if team == row[1]:
#                 list_of_years.append(row[0])
        
#         return list_of_years

# print(years_won('Los Angeles Lakers'))

# csv.dictreader() instead

def years_won(team):
    with open('nba_finals.csv', newline='') as csvfile:
        nba_file_dict = csv.DictReader(csvfile, delimiter=',')

        list_of_years = []

        for row in nba_file_dict:
            if team == row['Winner']:
                list_of_years.append(row['Year'])
        
        return list_of_years

print(years_won('Los Angeles Lakers'))
