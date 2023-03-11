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
    total_votes = 0
    candidates = []
    candidate_votes = {}
    result = ""
    winner = []
    winner_votes = 0
    output = {}

    # Read through each row in the CSV file
    for row in csvreader:

    #Calculate total votes
        total_votes += 1
      
    # Find list of candidates and calculate the total number each candidate won
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1
   
# Write results to csv file
with open(results, 'w') as file:

    file.write("Election Results\n")
    file.write("---------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("----------------------\n")
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}") 
    
    # Find the percentage of votes each candidate won and write the results in the csv file
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percent = (int(votes)/int(total_votes)) * 100
        output = (f'{candidate} : {votes} ({percent:.3f}%)')
        print(output)
        file.write(f'{output}\n' )

        #Find the winner and write in the csv file
        if (votes > winner_votes):
            winner_votes = votes
            winner = candidate
    print(f'Winner: {winner}')       
    file.write("-----------------------\n")
    file.write(f'Winner: {winner}')
  
   

    # print("Election Results")
    # print("----------------------------")
    # print(f"Total Votes: {total_votes}")
    # print("----------------------------")
    # print(output)
    # print("-----------------------------")
    # print(f'Winner : {winner}')


# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette