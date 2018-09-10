
import csv
import os

fname= './budget_data.csv'
date=[]
prolo=[]
nettotal=0
cprolo=[]
increase=[]
decrease=[]
with open(fname) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        date.append(row[0])
        prolo.append(row[1])
        nettotal= nettotal + float(row[1])
    for i in range(1,len(prolo)):
        cprolo.append(float(prolo[i])-float(prolo[i-1]))

length= len(date)

ave= sum(cprolo)/len(cprolo)
ave = round(ave,2)
maximum= max(cprolo)
minimum= min(cprolo)
maxindex= cprolo.index(maximum)
minindex= cprolo.index(minimum)
maxdate=date[maxindex+1]
mindate=date[minindex+1]

totalmonths= length

print("Financial Analysis")
print("--------------------------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${nettotal} ")
print(f"Average Change: ${ave}")
print(f"Greatest increase in profits:{maxdate} ${maximum} ")
print(f"Greatest decrease in profits:{mindate} ${minimum} ")

output_path = os.path.join("new.csv")

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis",''])
    csvwriter.writerow(["--------------------------------------------", ''])
    csvwriter.writerow([f"Total Months: {totalmonths}", ''])
    csvwriter.writerow([f"Total: ${nettotal}", ''])
    csvwriter.writerow([f"Average Change: ${ave}", ''])
    csvwriter.writerow([f"Greatest increase in profits:{maxdate} ${maximum}", ''])
    csvwriter.writerow([f"Greatest decrease in profits:{mindate} ${minimum}", ''])
