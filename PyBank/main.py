#Import modules
import os
import csv

#set path to the csv file
data = os.path.join("resources","data.csv") 

#Set the output for the results file
results = os.path.join("Analysis", "results.csv")

#Reading in the csv file
with open(data, "r") as file:

#CSV reader specifies delimiter and variable that hold contents
    csvreader=csv.reader(file, delimiter=',')

#Skip the header row
    header = next(csvreader)

#Set the variables   
    months_count=0
    total_profit = 0
    previous_profit = None
    changes = []
    greatest_increase=0
    greatest_month=""
    greatest_decrease=0
    decrease_month=""

    # Reading each row in the CSV file
    for row in csvreader:
        
        #Count the months
        months_count += 1

        # Get the current profit/loss value
        current_profit = int(row[1])

        # Add the current profit/loss value to the running total
        total_profit += current_profit

        # Calculate the change in profit/loss, find the greatest increase profit and greatest decrease in profit (date and amount)
        if previous_profit is not None:
            change = current_profit - previous_profit
            if change > greatest_increase:
                greatest_increase = change
                greatest_month = (row[0])
            if change < greatest_decrease:
                greatest_decrease = change
                decrease_month = (row[0])
            changes.append(change)
  
        # Update the previous profit/loss value for the next
        previous_profit = current_profit

    # Calculate the average change in profit/loss
    average_change = sum(changes) / len(changes)


    # Print the results
    print("Financial Analysis")
    print("--------------------------------------")
    print(f'Total months: {months_count}')
    print(f"Total Profit/Losses: ${total_profit}")
    print(f"Average Change: ${average_change:.2f}")
    print(f'Greatest increase in profits:{greatest_month, greatest_increase}')
    print(f'Greatest decrease in profits:{decrease_month, greatest_decrease}')

# Write results to csv file
with open(results, 'w') as file:

    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write(f"Total Months: {months_count}\n")
    file.write(f"Total Profit/Losses: ${total_profit}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits:{greatest_month, greatest_increase}\n")
    file.write(f"Greatest Decrease in Profits:{decrease_month, greatest_decrease}\n")

#The analysis should align with the following results:
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)