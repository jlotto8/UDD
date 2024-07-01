
# [ ] Print out a ranking of who has won the MVP more than once, by times won, e.g. this output:
#     - 6 times: Michael Jordan
#     - 3 times: Shaquille O'Neal, LeBron James
#     - 2 times: <etc>

"""
The first part of the problem to look at all the MVPs, put them in a dictionary, and count how many times each name appears. 
The next part is to organize the data- the counts of each MVP by descending order, which is made difficult because I don't know how to sort
When the data is sorted, it is in descending order, but ties are each on a new line
The last part is formatting the data so the ouput is the same as the example
When there are ties, each MVP name needs to go on the same line if MVP count is a tie
"""

"""
create an empty dictionary
loop through the csv
check if mvp is in the dictionary, if it is not
    add each mvp to the dictionary; mvp is key, the value will be 1
    if mvp is in the dictionary += 1 to the value
"""

import csv

with open('../Practice Problems/Project Underdog/NBA Finals/nba_finals.csv', newline='') as csvfile:
        nba_file_dict = csv.DictReader(csvfile, delimiter=',')

        mvp_dictionary = {}

        for row in nba_file_dict:
            name = row['MVP']
            if len(name)>1:
                if name in mvp_dictionary:
                    mvp_dictionary[name] += 1
                else:
                    mvp_dictionary[name] = 1
        # print(mvp_dictionary)

# homework finish this
        sorted_mvps = (sorted(mvp_dictionary.items(), key=lambda item: -item[1]))

        highest_mvp_wins = 500
        for mvp, current_wins in sorted_mvps:
            if current_wins < highest_mvp_wins:
                highest_mvp_wins = current_wins
                print()
                print(current_wins, mvp, end=" ")
                # print(end="")
            elif highest_mvp_wins == current_wins:

                print(mvp, end=" ")

"""
if wins has 

"""
wins = {"mike":2, "jessica": 3, "anna": 3}

finish = {2: ['mike'], 3: ['jessica','anna']}

order = 3,2

