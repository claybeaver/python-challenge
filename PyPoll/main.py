# Modules
import os
import csv

# Variables
vote_total = 0
cand_dict = {}
cand_total = 0
winner_val = 0
winner = ""

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
        #
        cand_name = str(row[2])
        # Compile the key value dictionary of candidates and their total votes
        if cand_name not in cand_dict:
            cand_dict[cand_name] = 1
        else: 
            cand_dict[cand_name] += 1
            
# Data Output
print("Election Results")
print("------------------------")
print(f'Total Votes: {vote_total}')
print("------------------------")
# For loop to add Candidate Percentage and Winner into output
for key,val in cand_dict.items():
    cand_perc = round((val / vote_total) * 100, 2)
    print(f'{key}: %{cand_perc:.3f} ({val})')
    if cand_perc > winner_val:
        winner_val = cand_perc
        winner = key    
print("------------------------")
print(f'Winner: {winner}')
print("------------------------")

#Data Output into Text File
with open("OutputAnalysis2.txt", "a") as e:
    print("Election Results", file = e)
    print("------------------------", file = e)
    print(f'Total Votes: {vote_total}', file = e)
    print("------------------------", file = e)
    for key,val in cand_dict.items():
        cand_perc = round((val / vote_total) * 100, 2)
        print(f'{key}: %{cand_perc:.3f} ({val})', file = e)
        if cand_perc > winner_val:
            winner_val = cand_perc
            winner = key    
    print("------------------------", file = e)
    print(f'Winner: {winner}', file = e)
    print("------------------------", file = e)