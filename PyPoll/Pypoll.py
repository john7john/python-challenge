import csv

path  = r"C:\Users\Smooth\Documents\GitHub\python-challenge\PyPoll\Resources\election_data.csv"
print("Election Results")
print("------------------")

candi = []
can1 = []
can2 = []
can3 = []
candidate = []
with open(path,"r") as csvf:
    csvreader = csv.reader(csvf, delimiter=',')
    header = next(csvreader)

    j=0
    for row in csvreader:
        bid = row[0]
        county = row[1]
        candid = row[2]
        candi.append(row[2])
        j+=1
    for x in candi:
        if x not in candidate:
            candidate.append(x)
        
    for can in candi:
        if candidate[0] == can:
            can1.append(can)
        if candidate[1] == can:
            can2.append(can)
        if candidate[2] == can:
            can3.append(can)

    
    can1p = (len(can1)/j)*100
    can2p = (len(can2)/j)*100
    can3p = (len(can3)/j)*100
    print("%.3f%%" % (can1p))
    print("%.3f%%" % (can2p))
    print("%.3f%%" % (can3p))

    print(f"Total Votes :{j}")
    print("--------------")    
        
    print(f"{candidate[0]} : {len(can1)}    "    "%.3f%%" % (can1p))
    print(f"{candidate[1]} : {len(can2)}    "     "%.3f%%" % (can2p))
    print(f"{candidate[2]} : {len(can3)}    "    "%.3f%%" % (can3p))

    print("--------------")   
    




    
    

        
