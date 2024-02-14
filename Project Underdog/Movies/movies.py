import csv

movies_data = []

with open('./top_movies.csv') as movies_data_csv:
    reader = csv.DictReader(movies_data_csv)

    for row in reader:
        movies_data.append(row)

# print(movies_data)