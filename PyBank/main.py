# Modules
import os
import csv

# Variables
num_rows = 0
total_pnl = 0

# Import budget_data.csv
# Set path for file
budget_data_path = os.path.join("Resources", "budget_data.csv")


# Read in the CSV file
with open(budget_data_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # # Average Change data
    # starting_num = [0][1]
    # final_num = [len(csvreader)][1]
    # print(starting_num)
    # print(final_num)



    for row in csvreader:
        num_rows += 1
        total_pnl += int(row[1])


    # # Testing printing our Budget Data information
    # print(csvreader)
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # for row in csvreader:
    #     print(row)



# # Data Output
# Average_Change = (final_num - starting_num) / (num_rows - 1)
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {num_rows}')
print(f'Total: ${total_pnl}')
# print(f'Average Change: ${round(Average_Change, 2)}')

