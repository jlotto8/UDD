# What are the longest baby names in the top 40 baby names for 2020? Make sure you can handle if there’s a tie.

"""
create a list to hold results
create a variable = 0
loop through the file
if len(name) > 0
variable = len(name)
list = [name]
if len(name) > len(biggest name)
append(name) to list

look at each name, check the number of letters in the name
compare each name length to the next name
when I encounter a name that is longer than the previous name, note it
if there is a name length == to the current longest name, add it to the noted name
keep checking each name, if a longer name appears, disregard the noted names
and note the new longest name
continue to the end of names
print all the noted names
"""
# review with open(); verbalize the problem, how to do it; running total, initialization case, branching

file_name = 'babynames_2020.txt'
file_handle = open(file_name)

longest_baby_names_list = []
longest_name_length = 0

for line in file_handle:
    current_baby_name = line.strip()

    if len(current_baby_name) > longest_name_length:
        longest_name_length = len(current_baby_name)
        longest_baby_names_list = [current_baby_name]
    elif len(current_baby_name) == longest_name_length:
        longest_baby_names_list.append(current_baby_name)
    elif len(current_baby_name) < longest_name_length:
        continue

print(longest_baby_names_list)


