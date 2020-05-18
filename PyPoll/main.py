# Modules
import os
import csv

# Variables
row_vote = 0
vote_total = 0

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
    
print(f'Total Votes: {vote_total}')

