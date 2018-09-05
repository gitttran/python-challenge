
import csv

csvpath ='./budget_data.csv'
date = []
prolo=[]
total = 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        date.append(row[1])
        prolo.append(row[2])
        total += prolo
