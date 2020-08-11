import os
import csv

electiondata_csv = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

voter_id=[]
county = []
candidates=["Khan", "Correy", "Li", "O'Tooley"]



with open(electiondata_csv) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=",")
    next(csv_reader, None)

    for row in csv_reader:
        voter_id.append(row[0])
        total_votes = len(voter_id)








print ("Election Results")
print("---------------------------------------")
print ("Total Votes: " + str(total_votes))
print("---------------------------------------")
print("Khan: ")
print ("Correy: ")
print("Li: ")
print("O'Tooley: ")
print("---------------------------------------")
print("Winner: ")
print("---------------------------------------")