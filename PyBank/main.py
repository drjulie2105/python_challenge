import os
import csv

budgetdata_csv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

profit_loss=[]
date = []
greatest_increase_month=[]
greatest_decrease_month=[]

with open(budgetdata_csv) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=",")
    next(csv_reader, None)

    for row in csv_reader:
        profit_loss.append(int(row[1]))
        date.append(row[0])
        months = len(date)
        total_profitloss=sum(profit_loss, 0)
        average_change = round(total_profitloss/months)

    
greatest_increase = max(profit_loss)
greatest_decrease = min(profit_loss)

greatest_increase_month=max(profit_loss), row[0]
greatest_decrease_month=min(profit_loss), row[0]



print ("Financial Analysis")
print("---------------------------------------")
print("Total Months: " + str(months))
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
    file.write("Total Months: " + str(months))
    file.write("\n")
    file.write("Total: $" + str(total_profitloss))
    file.write("\n")
    file.write("Average Change: $" + str(average_change))
    file.write("\n")
    file.write(f"Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease) + ")")