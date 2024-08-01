# What is the shortest baby name in the top 40 baby names for 2020?

"""
shortest_list = [] create a list- add the result to

create a variable with a large value
loop through each name
    if len(name) < variable:
        reset the variable to the shortest
        add the name to the list
return/print the list
"""

fn = 'babynames_2020.txt'
fh = open(fn)

shortest_list = []
short = 200000

for line in fh:
    line = line.strip()
    if len(line) < short:
        short = len(line)
        shortest_list = [line]
    elif short == len(line):
        shortest_list.append(line)
print(shortest_list)

# work on variable names
# re-write with more descriptive variable names
# lookupu resources on open()