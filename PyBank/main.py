import os
import csv

budgetdata_csv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

profit_loss=[]
date = []
changes = []
months = []

number_month = 0
net_profitloss = 0
last_month_profitloss = 0
this_month_profitloss = 0
change = 0

with open(budgetdata_csv) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=",")
    next(csv_reader, None)

    for row in csv_reader:
        profit_loss.append(int(row[1]))
        date.append(row[0])
        total_months = len(date)
        total_profitloss=sum(profit_loss, 0)


        number_month += 1
        this_month_profitloss = int(row[1])
        net_profitloss += this_month_profitloss

        if (number_month==1):
            last_month_profitloss = this_month_profitloss
            continue
        
        else:
            change = this_month_profitloss - last_month_profitloss
            months.append(row[0])
            changes.append(change)
            last_month_profitloss = this_month_profitloss
        
        sum_changes = sum(changes)
        average_change = round(sum_changes/(number_month-1), 2)
        greatest_increase = max(changes)
        greatest_decrease = min(changes)
        greatest_increase_index=changes.index(greatest_increase)
        greatest_decrease_index=changes.index(greatest_decrease)
        greatest_increase_month=months[greatest_increase_index]
        greatest_decrease_month=months[greatest_decrease_index]
        

print("Financial Analysis")
print("---------------------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profitloss))
print("Average Change: $" + str(average_change))
print(f"Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")")
print(f"Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease) + ")")

output_file=os.path.join("summary.txt")

with open(output_file, "w") as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("---------------------------------------")
    file.write("\n")
    file.write("Total Months: " + str(total_months))
    file.write("\n")
    file.write("Total: $" + str(total_profitloss))
    file.write("\n")
    file.write("Average Change: $" + str(average_change))
    file.write("\n")
    file.write(f"Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease) + ")")