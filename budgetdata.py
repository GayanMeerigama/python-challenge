from telnetlib import theNULL
import pandas as pd
import numpy as np

data = pd.read_csv("/Users/gayanmeerigama/Creative Cloud Files/Data Analytics Boot Camp/Assingnment3/PyBank/Resources/budget_data.csv")

f = open('out.txt','w',encoding='utf-8')


data.columns = ["date", "ProfitOrLosses"]
rawlist = list(data.ProfitOrLosses)

rawdate = list(data.date)

The_net_total_amount_of_Profit_Losses = sum(rawlist)

total_number_of_months = len(rawdate)

Greatest_increase_in_profits =  data['ProfitOrLosses'].max()

profitLossesList = list(data['ProfitOrLosses'])
dateProfitLossesList = data['date']

listOfChange =[]
count = 0

profitorlostdata = np.array(profitLossesList)
dateProfitLosses = np.array(dateProfitLossesList)


for i in range(len(data)-1):
    current = profitLossesList[i]
    currDown = profitLossesList[i+1]
    listOfChange.append(currDown-current)
    counter = sum(data['ProfitOrLosses'])

minChange = min(listOfChange)
maxChange = max(listOfChange)  
avgChance = round(np.mean(listOfChange),2)

maxChangeMonth = dateProfitLossesList[listOfChange.index(maxChange)+ 1] 

minChangeMonth = dateProfitLossesList[listOfChange.index(minChange) +1] 

date = ""



f.write(f"Financial Analysis\n----------------------------------\n")
#f.write(f"Your profit is: $\n",The_net_total_amount_of_Profit_Losses)
#f.write(f"Total Months \n",total_number_of_months)
#f.write(f"Average  Change: $\n",avgChance)
#f.write(f"Greatest Increase in Profits: ($)\n",maxChangeMonth,maxChange)
#f.write(f"Greatest Decrease in Profits: ($)\n",minChangeMonth,minChange) 

print("\nFinancial Analysis\n----------------------------------\n")

print("Total Months ",total_number_of_months)
print("Total: $",The_net_total_amount_of_Profit_Losses)
print("Average  Change: $",avgChance)
print("Greatest Increase in Profits: ($)",maxChangeMonth, maxChange)
print("Greatest Decrease in Profits: ($)",minChangeMonth,minChange)






f.write("OUTPUT")

f.close()

