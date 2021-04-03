# import 
import os
import csv

#Path to read in
csvPath = os.path.join('..', 'Resources', 'budget_data.csv')

#empty list/variables 
totalMonth = []
totalProfit = []
changeProfit = []

#open the csv file 
with open(csvPath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)

    for row in csvreader:
        totalMonth.append(row[0])
        totalProfit.append(int(row[1]))

    for i in range(len(totalProfit)-1):
        changeProfit.append(totalProfit[i+1]-totalProfit[i])

#Max and Min of the Profits
MaxProfit = max(changeProfit)
MinProfit = min(changeProfit)

#Find the coresponding months to the Max and Min Profits/Losses
# add one because the index starts at 0
MaxMonth = changeProfit.index(max(changeProfit)) + 1
MinMonth = changeProfit.index(min(changeProfit)) + 1

#Format the results
output = (
    f"Financial Analysis \n"
    f"------------------------- \n"
    f"Total Months: {len(totalMonth)} \n"
    f"Total: {sum(totalProfit)} \n"
    f"Average Change: {sum(changeProfit)/ len(changeProfit):.2f} \n"
    f"Greatest increase in Profits: {totalMonth[MaxMonth]} (${(str(MaxProfit))}) \n"
    f"Greatest decrease in Profits: {totalMonth[MinMonth]} (${(str(MinProfit))}) \n"
)
#print output
print(output)
