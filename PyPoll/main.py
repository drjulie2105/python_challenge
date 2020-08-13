import os
import csv

electiondata_csv = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

voter_id=[]
county = []
candidates = []
khan=[]
correy=[]
li=[]
otooley=[]


with open(electiondata_csv) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=",")
    next(csv_reader, None)

    for row in csv_reader:
        voter_id.append(row[0])
        total_votes = len(voter_id)
        if row[2] == "Khan":
            khan.append(row[2])
        elif row[2] == "Correy":
            correy.append(row[2])
        elif row[2] == "Li":
            li.append(row[2])
        else:
            otooley.append(row[2])
        total_khan = len(khan)
        total_correy = len(correy)
        total_li = len(li)
        total_otooley = len(otooley)
        
        percent_khan = total_khan / total_votes
        percent_correy = total_correy / total_votes
        percent_li = total_li / total_votes
        percent_otooley = total_otooley / total_votes

        
        if total_khan > total_correy and total_li and total_otooley:
            winner="Khan"
        elif total_correy > total_khan and total_li and total_otooley:
            winner="Correy"
        elif total_li > total_khan and total_correy and total_otooley:
            winner="Li"
        else:
            winner="O'Tooley"

print ("Election Results")
print("---------------------------------------")
print ("Total Votes: " + str(total_votes))
print("---------------------------------------")
print("Khan: " + "{:.3%} ".format(percent_khan) + "(" + str(total_khan) + ")")
print ("Correy: " + "{:.3%} ".format(percent_correy) + "(" + str(total_correy) + ")")
print("Li: " + "{:.3%} ".format(percent_li) + "(" + str(total_li) + ")")
print("O'Tooley: " + "{:.3%} ".format(percent_otooley) + "(" + str(total_otooley) + ")")
print("---------------------------------------")
print("Winner: " + str(winner))
print("---------------------------------------")

output_file=os.path.join("election_results.txt")

with open(output_file, "w") as file:

    file.write("Election Results")
    file.write("\n")
    file.write("---------------------------------------")
    file.write("\n")
    file.write("Total Votes: " + str(total_votes))
    file.write("\n")
    file.write("---------------------------------------")
    file.write("\n")
    file.write("Khan: " + "{:.3%} ".format(percent_khan) + "(" + str(total_khan) + ")")
    file.write("\n")
    file.write("Correy: " + "{:.3%} ".format(percent_correy) + "(" + str(total_correy) + ")")
    file.write("\n")
    file.write("Li: " + "{:.3%} ".format(percent_li) + "(" + str(total_li) + ")")
    file.write("\n")
    file.write("O'Tooley: " + "{:.3%} ".format(percent_otooley) + "(" + str(total_otooley) + ")")
    file.write("\n")
    file.write("---------------------------------------")
    file.write("\n")
    file.write("Winner: " + str(winner))
    file.write("\n")
    file.write("---------------------------------------")
