import os
import pandas as pd

# ingest
filepath = os.path.join("Resources","budget_data.csv")
os.path.isfile(filepath)
df = pd.read_csv(filepath)
pl = df['Profit/Losses']
df['diff'] = pl.diff()

# calculate
total_months = len(df)
total_profit_loss = pl.sum()
average_change = pl.diff().mean()
greatest_increase_row = df[pl.diff() == pl.diff().max()]
greatest_decrease_row = df[pl.diff() == pl.diff().min()]

# print
f = r'{:,.2f}' # number format
print('Financial Analysis')
print('----------------------------')
print('Total Months:', total_months)
print('Total:', f.format(total_profit_loss))
print('Average Change:', f.format(average_change))
print(
    'Greatest Increase in Profits:',
    greatest_increase_row['Date'].values[0],
    f.format(greatest_increase_row['diff'].values[0]))
print(
    'Greatest Decrease in Profits:',
    greatest_decrease_row['Date'].values[0],
    f.format(greatest_decrease_row['diff'].values[0]))