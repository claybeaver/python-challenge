# Modules
import os
import csv

# Variables
num_rows = 0
total_pnl = 0
starting_balance = 0
last_balance = 0
greatest_prof = 0
greatest_loss = 0
greatest_prof_date = ""
greatest_loss_date = ""

# Import budget_data.csv
# Set path for file
budget_data_path = os.path.join("Resources", "budget_data.csv")

# Read in the CSV file
with open(budget_data_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header row
    csv_header = next(csvreader)
    
    # Initialize the for loop for csvreader (which is budget_data.csv)
    for row in csvreader:
        # Set row_data equal to the current Profit/Loss in the loop
        row_data = int(row[1])
        # Set the starting_balance variable equal to the first Profit/Loss (row 2, column 2) in our data set
        # This will be used for the Average Change function later
        if num_rows == 0:
            starting_balance = row_data
        # Add 1 to the num_rows variable, and store it back into num_rows
        # This will simply keep track of the Total Months
        num_rows += 1
        # Continuously add the Profit/Loss of each loop (row_data) to the Total Profit/Loss (total_pnl)
        total_pnl += row_data
        # Run an if statement to keep track of the Greatest Increase/Loss in Profits
        pnl = row_data - last_balance
        if pnl > 0 and pnl > greatest_prof:
            greatest_prof = pnl
            # Record the string of the Date relating to the Greatest Increase in Profits
            greatest_prof_date = str(row[0])
        elif pnl <= 0 and pnl < greatest_loss:
            greatest_loss = pnl
            # Record the string of the Date relating to the Greatest Loss in Profits
            greatest_loss_date = str(row[0])
        # Set the last balance equal to the current row_data for the next for loop, so it will stay one behind
        last_balance = row_data


# Data Output
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {num_rows}')
print(f'Total: ${total_pnl}')
print(f'Average Change: ${round((last_balance - starting_balance) / (num_rows - 1), 2)}')
print(f'Greatest Increase in Profits: {greatest_prof_date} (${greatest_prof})')
print(f'Greatest Decrease in Profits: {greatest_loss_date} (${greatest_loss})')

# Data Output into Text File
with open("OutputAnalysis.txt", "a") as f:
    print("Financial Analysis", file=f)
    print("----------------------------", file=f)
    print(f'Total Months: {num_rows}', file=f)
    print(f'Total: ${total_pnl}', file=f)
    print(f'Average Change: ${round((last_balance - starting_balance) / (num_rows - 1), 2)}', file=f)
    print(f'Greatest Increase in Profits: {greatest_prof_date} (${greatest_prof})', file=f)
    print(f'Greatest Decrease in Profits: {greatest_loss_date} (${greatest_loss})', file=f)