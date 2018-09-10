import csv
import os

fname='./election_data.csv'
VoterID=[]
County=[]
Candidate=[]
ucan=[]
votes=[]

with open(fname) as csvfile:
    csvreader=csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        VoterID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

    for can in Candidate:
        if can not in ucan:
            ucan.append(can)
            votes.append(0)

numcan=len(ucan)
for i in Candidate:
    for j in range(numcan):
        if i == ucan[j]:
            votes[j]+=1

win=max(votes)
winindex= votes.index(win)
winner=ucan[winindex]
totalvotes=len(VoterID)

print("Election Results")
print("-------------------------")
for r in range(len(ucan)):
    print(f"{ucan[r]}: {'{0:.3%}'.format(votes[r]/totalvotes)} ({votes[r]})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

output_path = os.path.join("new.csv")

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results",''])
    csvwriter.writerow(["-------------------------", ''])
    for r in range(len(ucan)):
        csvwriter.writerow([f"{ucan[r]}: {'{0:.3%}'.format(votes[r]/totalvotes)} ({votes[r]})", ''])
    csvwriter.writerow([f"-------------------------", ''])
    csvwriter.writerow([f"Winner: {winner}", ''])
    csvwriter.writerow(["-------------------------", ''])
