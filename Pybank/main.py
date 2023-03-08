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
    dic = []
    
    profit = []
    data = []
    for row in csvreader:
        
        date = row[0]
        pl = int(row[1])

        months +=1
        sum = pl + sum 
        profit.append(pl)
    
    for j in range(len(profit)):
        diff = profit[j] - profit[j-1]
        dic.append(diff)
    dic.pop(0)
    
    for k in range(len(dic)):
        sum1 = dic[k] + sum1
    avg = sum1/len(dic)
    
    lrg = dic[0]
    start = dic[0]
    for g in range(len(dic)):               
        if start < dic[g-1]:
            start = dic[g-1]
        if  lrg > dic[g-1]:
            lrg = dic[g-1]  
        
    






    
    
    print(f"Total Months :{months}")
    print(f"Total  :${sum}")
    print(f"Average Change  :{avg}")
    print(f"Greatest Increase in Profits:{start}")
    print(f"Greatest Decrease in Profits:{lrg}")
   
        
        
       

       
