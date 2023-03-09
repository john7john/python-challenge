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

    arr=[]

    # prev_net=int(header[1])

    for row in csvreader:

        # print(row[1])
        # net_change=int(row[1])-prev_net
        # prev_net=int(row[1])
        # arr+=[net_change]
        # date = row[0]
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
    avg = sum1/len(diffc)
    # print(diffc)
    


    low = diffc[0]
    high = diffc[0]
    
    for g in range(len(diffc)):               
        if high < diffc[g-1]:
            high = diffc[g-1]
    


        if  low > diffc[g-1]:
            low = diffc[g-1]  
    
       
    # for r in final:
    #      f = r[0]
    #      sec = r[1]
    #      if r[1] == low:  
    
        







    
    
    print(f"Total Months :{months}")
    print(f"Total  :${sum}")
    print(f"Average Change  :{avg}")
    print(f"Greatest Increase in Profits:{high}")
    print(f"Greatest Decrease in Profits:{low}")
   
        
        
       

       
