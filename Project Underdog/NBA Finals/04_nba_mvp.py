
# [ ] Print out a ranking of who has won the MVP more than once, by times won, e.g. this output:
#     - 6 times: Michael Jordan
#     - 3 times: Shaquille O'Neal, LeBron James
#     - 2 times: <etc>
"""
create a dictionary to store the MVP names, and amount of times the names appear
open the csv
loop through each row
check if mvp is blank:
if mvp is not blank:
    add 1 to the dictonary value

create a list of tuples
make each key value pair a tuple
create a lamba function to sort by the amount of times mvp appears; reverse it

loop through each tuple
print the output
"""

import csv
from collections import Counter

mvp_dictionary = Counter()

with open('nba_finals.csv', newline='') as csvfile:
        nba_file_dict = csv.DictReader(csvfile, delimiter=',')


        for row in nba_file_dict:
            if row['MVP']: 
                mvp_dictionary.update([row['MVP']])

        tuples = mvp_dictionary.items()

        sorted_tuples = sorted(tuples,key=lambda t:-t[1])
        # print(sorted_tuples)
        """
        if the second item in the tuple is less than the previous one, print on a new line
        if the number is the same, print on the same line
        """

        # infinity 
        previous_count = float('inf')
        for player, current_count in sorted_tuples:
            if current_count >1:
                if current_count < previous_count:
                    if previous_count != float('inf'):
                        print("")
                    print(f' - {current_count} times: {player}', end="")
                    previous_count = current_count
               
                else:
                    print(f', {player}', end="")
        print()

# homework- how to remove the extra blank line; % at the end of the output = did not produce a new line; only print if mvp has won >1 time
# used a conditional to check the loop was checking anything, if not, do not print
# looked back at the question prompt- it only asks for mvp who have won >1 x
# if I had to do it, I would do this:  elif previous_count == 1:
                    # print(f', - {current_count} time: {player}',end="")
# am i supposed to get rid of the final % char?