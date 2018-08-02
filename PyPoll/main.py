import os
import csv
#import counting functions
from collections import Counter

# Assigning initial variables
vote_count = 0
candidate_list = []
path_file = '/Users/alnunu/repos/python-challenge/election_data.csv'

# Open and read csv
with open(path_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first 
    csv_header = next(csvfile)
    # Read through each row of data after the header
    for row in csvreader:
        # Count the total number of votes
        vote_count = vote_count+1
        # Create list of candidates
        candidate_list.append(row[2])

#deteriming winning candidate
v = list(Counter(candidate_list).values())
k = list(Counter(candidate_list).keys())
winner = k[v.index(max(v))]

#print vote analysis
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(vote_count))
print("-------------------------")
# find/print unique values in candidate list and count candidate vote frequency
for candidate, vote in Counter(candidate_list).items():
    print(candidate + ": " + "{:.3%}".format(vote/vote_count) +" (" + str(vote) + ")")
print("-------------------------")
print("Winner: " + (winner))

#create txt file
file = open("PyPoll.txt","w")
file.write("Election Results\n")
file.write("-------------------------\n")
file.write("Total Votes: " + str(vote_count) + "\n")
file.write("-------------------------\n")
for candidate, vote in Counter(candidate_list).items():
    file.write(candidate + ": " + "{:.3%}".format(vote/vote_count) + " (" + str(vote) + ")\n")
file.write("-------------------------\n")
file.write("Winner: " + (winner))
file.close()