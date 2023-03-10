PyBank  --------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------  

import csv

filepath = r"C:\Users\Smooth\Documents\GitHub\python-challenge\Pybank\Resources\budget_data.csv"
print("Financial Analysis ")
print("-----------------------------")

with open(filepath, 'r') as csvf:
            
    k= 0
    csvreader = csv.reader(csvf, delimiter=',')                 # Reading CSV
    header = next(csvreader)
    months = 0
    sum1 = 0
    sum = 0
    diffc = []
    date= []
    profit = []
    data = []
    
    for row in csvreader:
        pl = int(row[1])
        months +=1
        sum = pl + sum                  # Seperating csv data into profit and date
        profit.append(pl)
        date.append(row[0])
    
    for j in range(len(profit)):            #finding average change of each month and appending changes to diffc
        diffc.append(profit[j] - profit[j-1])
    diffc.pop(0)
    
    for k in range(len(diffc)):             #finding average change 
        sum1 = diffc[k] + sum1
    avg = round(sum1/len(diffc),2)
    # print(diffc)
    
    low = diffc[0]
    high = diffc[0]
    indexhigh = 0
    indexlow = 0
   
    for g in range(len(diffc)):               # Finding highest average change
        if high < diffc[g-1]:
            high = diffc[g-1]
            indexhigh = g


        if  low > diffc[g-1]:                   # Finding lowest average change
            low = diffc[g-1]  
            indexlow = g
     
    print(f"Total Months :{months}")
    print(f"Total  :${sum}")
    print(f"Average Change  :${avg}")
    print(f"Greatest Increase in Profits:{date[indexhigh]} (${high})")
    print(f"Greatest Decrease in Profits:{date[indexlow]} (${low})")
    
    with open("Pybank\Analysis\Financial Analysis.txt","w") as out:                # Printing output to txt
        writer = csv.writer(out)
        writer.writerow(["Financial Analysis"])
        writer.writerow(["--------------------"])
        writer.writerow([(f"Total Months :{months}")])
        writer.writerow([(f"Total  :${sum}")])
        writer.writerow([(f"Average Change  :${avg}")])
        writer.writerow([(f"Greatest Increase in Profits:{date[indexhigh]} (${high})")])
        writer.writerow([f"Greatest Decrease in Profits:{date[indexlow]} (${low})"])
        



PyPoll---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------
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
    