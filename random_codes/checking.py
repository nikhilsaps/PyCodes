import csv


with open('username.csv','r') as csvfile:
    csvread= csv.reader(csvfile)

    fields = next(csvread)
    print(fields)

