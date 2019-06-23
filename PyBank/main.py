#Import OS for pathing and CSV to read .csv format
import os
import csv

#set file path to a variable
Budget_csv = os.path.join("budget-data.csv")

#Read the csv into a variable
with open(Budget_csv, newline='') as csvfile:
    csvbudget = csv.reader(csvfile, delimiter=',')
    next(csvfile)#skip header

    #create some variables and default values
    #total months and total profit/loss containers
    total_months = 0
    total_pl = 0
    #create a list container for the change of profit/loss, will convert later to int for calculations
    pl_change_list = []
    profit_change = []
    r = 0
    total_pl_var = 0

    #loop through the records to get the months and total profit/loss
    for row in csvbudget:
        total_months += 1
        total_pl = total_pl + int(row[1])
        
        #during loop, create list for the profit change and also a list in change_pl to show the difference between the next and current row
        profit_change.append(row[1])
        change_pl = int(profit_change[r]) - int(profit_change[r - 1])
        pl_change_list.append(change_pl)

        #find the max
        max_profit = max(pl_change_list)
        if  pl_change_list[r] == max_profit:
            max_month = row[0]
        
        #find the min
        min_profit = min(pl_change_list)
        if pl_change_list[r] == min_profit:
            min_month = row[0]
        
        #find the average total
        avg_var_pl = int(pl_change_list[r])
        total_pl_var += avg_var_pl    
        
        #increase our counter
        r += 1
    
    #find the average for the profit/loss total
    avg_pl = round(total_pl_var/ (total_months - 1), 2)


    #print results in console
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + str(total_pl))
    print("Average Change: " + str(avg_pl))
    print("Greatest Increase in Profits: " + str(max_month) + " (" + str(max_profit) + ")")
    print("Greatest Decrease in Profits: " + str(min_month) + " (" + str(min_profit) + ")")

    with open("budget_data.txt", 'w') as text_file:
        print("Financial Analysis", file = text_file)
        print("----------------------------",file = text_file)
        print("Total Months:" + str(total_months), file = text_file)
        print("Total: $" + str(total_pl), file = text_file)
        print("Average Change: $" + str(avg_pl), file = text_file)
        print("Greatest Increase in Profits: " + str(min_month) + " (" + str(min_profit) + ")", file = text_file)
        print("Greatest Decrease in Profits: " + str(min_month) + " (" + str(min_profit) + ")", file = text_file)