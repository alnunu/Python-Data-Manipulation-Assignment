import os
import csv

# Assigning initial variables
month_count = 0
total_pl = 0
rev_list = []
revdif = []
date_list = []
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
        # Create list of revenues and dates to calculate changes later
        rev_list.append(row[1])
        date_list.append(row[0])

# Create difference in revenue list
for i in range(1,len(rev_list)):
    revdif.append(int(rev_list[i]) - int(rev_list[i-1])) 
    #calculate average change and round to two decimal points
    avg_change = format((sum(revdif)/len(revdif)), '.2f')
    #calculate max and min revenue change values
    greatest_profit = max(revdif)
    largest_loss = min(revdif)
    #retrieve date
    greatest_profit_month = str(date_list[revdif.index(max(revdif))+1])
    largest_loss_month = str(date_list[revdif.index(min(revdif))+1])

#Print Analysis
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(month_count))
print("Total: " + "$" + str(total_pl))
print("Average Change: " + "$" + (str(avg_change)))
print("Greatest Increase in Profits: " + greatest_profit_month + " ($" + str(greatest_profit)+ ")")
print("Greatest Decrease in Profits: " + largest_loss_month + " ($" + str(largest_loss)+ ")")