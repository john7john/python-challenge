import csv

filepath = r"C:\Users\Smooth\Documents\GitHub\python-challenge\Pybank\Resources\budget_data.csv"
print("Financial Analysis ")
print("-----------------------------")

with open(filepath, 'r') as csvf:
            
    k= 0
    csvreader = csv.reader(csvf, delimiter=',')
    header = next(csvreader)
    months = 0
    sum = 0
    total_change = 0
    diffc = []
    date= []
    profit = []
    


    for row in csvreader:

        
        pl = int(row[1])

        months +=1
        sum = pl + sum 
        profit.append(pl)
        date.append(row[0])
    
    for j in range(len(profit)):
        diff = profit[j] - profit[j-1]
        diffc.append(diff)
    print(sum(diffc)/len(diffc))
    diffc.pop(0)
    print(row[1:3])