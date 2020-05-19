# Modules
import os
import csv

# Variables
vote_total = 0
cand_name = ""
cand_list = []
cand_total = 0

# Import election_data.csv
# Set path for file
election_data_path = os.path.join("Resources", "election_data.csv")

# Read in the CSV file
with open(election_data_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header row
    csv_header = next(csvreader)

    # Initialize the for loop for csvreader (which is election_data.csv)
    for row in csvreader:
        # Set row_vote equal to the first vote
        vote_total += 1
        # Compile the list of candidates
        if str(row[2]) not in cand_list:
            cand_list.append(str(row[2]))
            cand_total += 1
        # Calculate % of votes each candidate won





print("Election Results")
print("------------------------")
print(f'Total Votes: {vote_total}')
print("------------------------")
# for cand_name in cand_list[0]:
#     print(cand_name,end='')
# for cand_name in cand_list[1]:
#     print(cand_name,end='')
# for cand_name in cand_list[2]:
#     print(cand_name,end='')
# for cand_name in cand_list[3]:
#     print(cand_name,end='')
