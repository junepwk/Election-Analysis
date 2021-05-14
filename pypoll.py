# The data we need to retrieve
# 1. The total nummber of votes cast
# 2. A complete list of candidates who received votes
# 3. The total number of votes each candidate won
# 4. The percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Import csv module
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Put here so everytime we run the file, total_votes variable is set to zero
total_votes = 0

#declare a list for candidate's names
candidate_options = []

#declare dictionary to store votes each candidate won
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results 
with open(file_to_load) as election_data:
    
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)
    
    #iterate through each row 
    for row in file_reader:

        #add up the total vote count
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        #add candaidate names to the candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #increment each candidate's vote by 1 every time a candidate name appears in a row
        candidate_votes[candidate_name] += 1

#Save results to our text file
with open(file_to_save, "w") as txt_file:

    election_results = (f'\nElection Results\n'
                        f'---------------------------\n'
                        f'Total Votes: {total_votes:,}\n'
                        f'---------------------------\n')

    print(election_results, end ="")

    txt_file.write(election_results)

    #Determine the percentage of votes for each candidate by looping through the counts
    #1. iterate through the candidate list
    for candidate_name in candidate_votes:

        #2. retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        #3. calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        #determine winning vote count and candidate
        #determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            #if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

            #set winning_candidate to the candidate's name
            winning_candidate = candidate_name


        candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

        print(candidate_results)

        #save the candidate results to our text file
        txt_file.write(candidate_results)
    
    winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
    print(winning_candidate_summary)
        
    #save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)