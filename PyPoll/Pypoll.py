import csv

path  = r"C:\Users\Smooth\Documents\GitHub\python-challenge\PyPoll\Resources\election_data.csv"
print("Election Results")
print("------------------")

candi = []
can1 = []
can2 = []
can3 = []
candidate = []
with open(path,"r") as csvf:                            # Reading csv file
    csvreader = csv.reader(csvf, delimiter=',')
    header = next(csvreader)

    j=0
    for row in csvreader:
              
        candi.append(row[2])
        j+=1
    for x in candi:
        if x not in candidate:          # j is the total number of votes 
            candidate.append(x)
        
    for can in candi:
        if candidate[0] == can:         #counting candidate votes
            can1.append(can)
        if candidate[1] == can:
            can2.append(can)
        if candidate[2] == can:
            can3.append(can)  
        

    canv1 = len(can1)
    canv2 = len(can2)
    canv3 = len(can3)
    can1p = (len(can1)/j)*100           #Finding % of votes
    can2p = (len(can2)/j)*100
    can3p = (len(can3)/j)*100
   

    print(f"Total Votes :{j}")
    
    print("--------------")    
        
    print(f"{candidate[0]} : {canv1}    ""%.3f%%" % (can1p))        #Printing results with % and count of votes
    print(f"{candidate[1]} : {canv2}    ""%.3f%%" % (can2p))
    print(f"{candidate[2]} : {canv3}    ""%.3f%%" % (can3p))

     

    print("--------------")   
    
    c1 = str
    if canv1 > canv2 and canv1 > canv3:                         #Selecting winner based on votes
        print(f" Winner is :{candidate[0]} ")
        c1 = (f" Winner is :{candidate[0]} ")
    if canv2 > canv1 and canv2 > canv3:
        print(f" Winner is :{candidate[1]} ")
        c1 = (f" Winner is :{candidate[1]} ")
    if canv3 > canv2 and canv3 > canv1:
        print(f" Winner is :{candidate[2]} ")
        c1 = (f" Winner is :{candidate[2]} ")
    print("--------------") 
with open("Pypoll\Analysis\Election result.txt","w") as out:                # Printing output to txt
    writer = csv.writer(out)
    writer.writerow(["Election Results"])
    writer.writerow(["------------------"])
    writer.writerow([f"Total Votes   :{j}"])
    writer.writerow([f"{candidate[0]} : {canv1}    ""%.3f%%" % (can1p)])
    writer.writerow([(f"{candidate[1]} : {canv2}    ""%.3f%%" % (can2p))])
    writer.writerow([(f"{candidate[2]} : {canv3}    ""%.3f%%" % (can3p))])
    writer.writerow([c1])
    
                    



    
    

        
