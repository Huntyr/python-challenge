#PyPoll: Help a town modernize their vote counting 

#import os for pathing and csv for reading .csv files
import os
import csv

#file path (Im still not great with the os.path.join() at all. todo)

voting_csv = "election_data.csv"

#open the csv and assign it to a variable
with open(voting_csv, newline='') as csvfile:
    csvvotes = csv.reader(csvfile, delimiter= ',')
    next(csvfile) #skip header
    
    #create some variables for the loop to use

    total_count = 0
    khan_num = 0
    correy_num = 0
    li_num = 0
    tooley_num = 0

    #loop through the list to get the number of votes for each candidate
    for row in csvvotes:
        total_count += 1
        if row[2] == "Khan":
            khan_num += 1
        elif (row[2] == "Correy"):
            correy_num += 1
        elif (row[2] == "Li"):
            li_num += 1
        elif (row[2] == "O'Tooley"):
            tooley_num += 1


#now for percentages: vote_count_individual/total_votes * 100 for percentages
khan_per = round(khan_num/total_count * 100)
correy_per = round(correy_num/total_count * 100)
li_per = round(li_num/total_count * 100)
tooley_per = round(tooley_num/total_count * 100)

contenders = {"Khan": khan_per, "Correy": correy_per, "Li": li_per, "O'Tooley": tooley_per}
winner = max(contenders, key=contenders.get)

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_count))
print("-------------------------")
print("Khan: " + str(khan_per) + "(" + str(khan_num) + ")")
print("Correy: " + str(correy_per) + "(" + str(correy_num) +")")
print("Li: " + str(li_per) + "(" + str(li_num) + ")")
print("O'Tooley: " + str(tooley_per) + "(" + str(tooley_num) + ")")
print("-------------------------")
print("Winner: " + winner)

#now export to txt file
with open("election_data.txt", "w") as txtfile:
    print("Election Results", file = txtfile)
    print("-------------------------", file = txtfile)
    print("Total Votes: " + str(total_count), file = txtfile)
    print("-------------------------", file = txtfile)
    print("Khan: " + str(khan_per) + "(" + str(khan_num) + ")", file = txtfile)
    print("Correy: " + str(correy_per) + "(" + str(correy_num) +")", file = txtfile)
    print("Li: " + str(li_per) + "(" + str(li_num) + ")", file = txtfile)
    print("O'Tooley: " + str(tooley_per) + "(" + str(tooley_num) + ")", file = txtfile)
    print("-------------------------", file = txtfile)
    print("Winner: " + winner, file = txtfile)
