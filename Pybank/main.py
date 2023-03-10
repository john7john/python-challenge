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
        