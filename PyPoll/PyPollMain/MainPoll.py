# import
import os
import csv

#read in csv
csvPath = os.path.join('..', 'Resources', 'election_data.csv')

#variables
totalVotes = 0
khanVotes = 0
corryVotes = 0
liVotes = 0
otooleyVotes = 0

#open csv file
with open(csvPath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    for row in csvreader:
        totalVotes += 1

        canidate = str(row[2])

        if canidate == "Khan":
            khanVotes += 1
        if canidate == "Correy":
            corryVotes += 1
        if canidate == "Li":
            liVotes += 1
        if canidate == "O'Tooley":
            otooleyVotes += 1
        
    canidateVote = {
        "Khan": khanVotes, "Correy": corryVotes, "Li": liVotes, "O'Tooley": otooleyVotes
        }
    if khanVotes > corryVotes and liVotes and otooleyVotes:
            #print("Khan is the Winner")
            winner = "Khan"
    if corryVotes > khanVotes and liVotes and otooleyVotes:
            #print("Correy is the Winner")
            winner = "Correy"
    if liVotes > khanVotes and corryVotes and otooleyVotes:
            #print("Li is the Winnner")
            winner = "Li"
    if otooleyVotes > khanVotes and corryVotes and liVotes:
            #print("O'Tooley is the Winner")
            winner = "O'Tooley"
    
    #precentages
    khanPercent = (khanVotes/totalVotes) *100
    corryPercent = (corryVotes/totalVotes) *100
    liPercent = (liVotes/totalVotes) *100
    otooleyPercent = (otooleyVotes/totalVotes) *100

#Format the Results total votes -1 i think it counted the header 
output = (
    f"Election Results\n"
    f"---------------------\n"
    f"Total Votes: {totalVotes - 1}\n"
    f"----------------------\n"
    f"Khan: {khanPercent:.2f}% ({khanVotes})\n"
    f"Correy: {corryPercent:.2f}% ({corryVotes})\n"
    f"Li: {liPercent:.2f}% ({liVotes})\n"
    f"O'Tooley: {otooleyPercent:.2f}% ({otooleyVotes})\n"
    f"------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)
#print the results
print(output)