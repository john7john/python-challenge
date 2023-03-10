import csv

filepath = r"C:\Users\Smooth\Documents\GitHub\python-challenge\Pybank\Resources\budget_data.csv"
print("Financial Analysis ")
print("-----------------------------")

with open(filepath, 'r') as csvf:
            
    k= 0
    csvreader = csv.reader(csvf, delimiter=',')
    header = next(csvreader)
    months = 0
    sum1 = 0
    sum = 0
    total_change = 0
    diffc = []
    date= []
    profit = []
    data = []
    d=[]
    final = []


    for row in csvreader:

        
        pl = int(row[1])

        months +=1
        sum = pl + sum 
        profit.append(pl)
        date.append(row[0])
    
    for j in range(len(profit)):
        diff = profit[j] - profit[j-1]
        diffc.append(diff)
    # print(sum(diffc)/len(diffc))
    diffc.pop(0)
    
    for k in range(len(diffc)):
        final.append([date[k],diffc[k]])
        sum1 = diffc[k] + sum1
    avg = round(sum1/len(diffc),2)
    # print(diffc)
    
    low = diffc[0]
    high = diffc[0]
    indexhigh = 0
    indexlow = 0

    
    for g in range(len(diffc)):               
        if high < diffc[g-1]:
            high = diffc[g-1]
            indexhigh = g


        if  low > diffc[g-1]:
            low = diffc[g-1]  
            indexlow = g
     
    print(f"Total Months :{months}")
    print(f"Total  :${sum}")
    print(f"Average Change  :${avg}")
    print(f"Greatest Increase in Profits:{date[indexhigh]} (${high})")
    print(f"Greatest Decrease in Profits:{date[indexlow]} (${low})")
    
   