import csv

filepath = r"C:\Users\Smooth\Desktop\Weekly Challenges\Python\Instructions\PyBank\Resources\budget_data.csv"

with open(filepath, 'r') as csvf:

    csvreader = csv.reader(csvf, delimiter=',')
    