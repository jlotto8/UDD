# What are all of the names that were top 40 baby names in both 1880 and 2020?

file_name_2020 = 'babynames_2020.txt'
file_handle_2020 = open(file_name_2020)

duplicate_names = []

for name in file_handle_2020:
    name = name.strip()

    file_name_1880 = 'babynames_1880.txt'
    file_handle_1880 = open(file_name_1880)

    for early_name in file_handle_1880:
        early_name = early_name.strip()
        if name == early_name:
            duplicate_names.append(early_name)
print(duplicate_names)







