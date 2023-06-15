import os
import pandas as pd

# ingest
wd = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(wd,'Resources','budget_data.csv')
df = pd.read_csv(filepath)
header_row = list(df.columns)
pl = df['Profit/Losses']

# transform
df['diff'] = pl.diff()

# calculate
total_months = len(df)
total_profit_loss = pl.sum()
average_change = pl.diff().mean()
inc_row = df[pl.diff() == pl.diff().max()]
dec_row = df[pl.diff() == pl.diff().min()]

# compose output text
f = r'{:,.2f}' # number format
output_text = \
f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: {f.format(total_profit_loss)}
Average Change: {f.format(average_change)}
Greatest Increase in Profits: {inc_row['Date'].values[0]} ({f.format(inc_row['diff'].values[0])})
Greatest Decrease in Profits: {dec_row['Date'].values[0]} ({f.format(dec_row['diff'].values[0])})
"""

# output
print(output_text)
output_file = os.path.join(wd,'output.txt')

with open(output_file, 'w') as txt:
    txt.write(output_text)

print('Saved to', output_file)