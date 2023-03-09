import csv

path  = r"C:\Users\Smooth\Documents\GitHub\python-challenge\PyPoll\Resources\election_data.csv"
print("Election Results")
print("------------------")
with open(path,"r") as csvf:
    csvreader = csv.reader(csvf, delimiter=',')
    header = next(csvreader)

    j=0
    for row in csvf:
        bid = row[0]
        county = row[1]
        candid = row[2]
        j+=1
    print(f"Total Votes :{j}")
    print("--------------")
    print(row[3].unique)
        
        
