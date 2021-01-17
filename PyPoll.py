import csv

import os

# Assign a variable for the file to load and path
file_to_load = os.path.join('Resources','election_results.csv')

# Open the election results and read the file
# with open(file_to_load) as election_data:
#     print(election_data)

# writing a file to a directory on the computer
# create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join('analysis','election_analysis.txt')

# 1. Initialize a total vote counter
total_votes = 0

# Candidate options
candidate_options = []

# Declare empty dictionary for votes by candidate
candidate_votes = {}

# Winning Candidate and Winning count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the file as a text file using the with statement
# outfile = open(file_to_save,'w') >> alternate way of opening the file
with open(file_to_load) as election_data:
    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Print each row in CSV file
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes += 1

        # Print the candidate name form each row
        candidate_name = row[2]

        # If the Candidate does not match any existing candidates
        if candidate_name not in candidate_options:
            # Add it to the list of candidates

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Beging tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save,'w') as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f'-----------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-----------------------------\n')
    print(election_results, end='')

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        # Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print each candidate's name, vote count and percentage of vote's 
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote and candidate
        # Determine if the votes is greater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    # Print the winning candidate's results to the terminal
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n"
    )

    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)














    # close the file

    # To do: perform analysis

    # Close the file

    # The data we need to retrieve

    # 1. The total number of votes cast

    # 2. Complete list of candidates who received votes

    # 3. Percentage of votes each candidate won

    # 4. Total number of votes each candidate won

    # 5. Winner of the election based on popular vote