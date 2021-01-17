import datetime

now = datetime.datetime.now()

print('The time right now is', now)

import csv

import random

import numpy

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

        # Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)

# 3. Print the total votes
print(total_votes)

# Print the candidate list
print(candidate_options)





# close the file

# To do: perform analysis

# Close the file

# The data we need to retrieve

# 1. The total number of votes cast

# 2. Complete list of candidates who received votes

# 3. Percentage of votes each candidate won

# 4. Total number of votes each candidate won

# 5. Winner of the election based on popular vote