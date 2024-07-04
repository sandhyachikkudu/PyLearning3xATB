import csv
with open('TD.csv') as csvfile:
    reader = csv.reader(csvfile)
    for column in reader:
        print(column[0],column[1],sep= " || ")