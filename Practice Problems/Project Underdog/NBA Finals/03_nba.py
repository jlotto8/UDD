# Which teams have made it to the NBA finals but have never won?
"""
possibilities:
    a. play in the finals and win
    b. play in the finals and lose

2. the team can not make it the NBA finals

condition is teams that are in the loser heading and not in the winner heading

create a set to hold the results of team names

use dictreader()
loop through dictionary which each row of the file
    loop through dictionary again
if the team name is in the loser heading
    if team name is in not in the winner heading
    keep track of the team name, by adding it to a list of results
return the set
"""

import csv


with open('nba_finals.csv', newline='') as csvfile:
        nba_file_dict = csv.DictReader(csvfile, delimiter=',')
        losing_teams = set()
        winning_teams = set()
        only_losers = set()

        for row in nba_file_dict:
            # if row ==['Winner']:
            winning_teams.add(row['Winner'])
            losing_teams.add(row['Loser'])

        for team in losing_teams:
            if team not in winning_teams:
                only_losers.add(team)
        print(only_losers)              

# write a formal, non-code explanation- 1. whaat is the problem 2, how do i solve it 3. what do i keep track of
# 4. how do i keep track of it/scope/through the loop, etc