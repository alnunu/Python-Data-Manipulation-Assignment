import os
import csv

# Assigning initial variables
pl_betweenmonths = []
month_count=0
total_pl=0
avg_change =0
greatest_profit = ["month", 0]
largest_loss = ["month", 0]
path_file = '../alnunu/repos/python-challenge/budget_data.csv'

# Open and read csv
with open(path_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)

    # Read through each row of data after the header
    for row in csvreader:
        # Count the total number of months
        month_count = month_count+1
        # Calculate total profit and loss
        total_pl=total_pl + int(row[1])
        # determing greatest profit and largest loss
        if int(row[1]) > greatest_profit[1]:
            greatest_profit = [row[0],int(row[1])]
        if int(row[1]) < largest_loss[1]:
            largest_loss = [row[0],int(row[1])]

#Print Analysis
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(month_count))
print("Total: " + "$" + str(total_pl))
print("Average Change: " + "$" + str(avg_change))
print("Greatest Increase in Profits: " + str(greatest_profit[0]) + " ($" + str(greatest_profit[1])+ ")")
print("Greatest Decrease in Profits: " + str(largest_loss[0]) + " ($" + str(largest_loss[1])+ ")")
