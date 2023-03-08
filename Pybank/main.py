import csv

filepath = r"C:\Users\Smooth\Documents\GitHub\python-challenge\Pybank\Resources\budget_data.csv"
print("Financial Analysis ")
print("-----------------------------")

with open(filepath, 'r') as csvf:
            

    csvreader = csv.reader(csvf, delimiter=',')
    header = next(csvreader)
    months = 0
    sum = 0
    
    for row in csvreader:
        
        date = row[0]
        pl = int(row[1])
        months +=1
        sum = pl + sum 
    avg = months/sum
    print(f"Total Months :{months}")
    print(f"Total  :${sum}")
    print(f"Total  :${avg}")

        
        # count=0
        # for item in date:
        #     count +=1
       
    
# print(f"Total Months :{months(date)}")
        
       
