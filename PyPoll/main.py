import os
import pandas as pd

# ingest
wd = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(wd,"Resources","election_data.csv")
df = pd.read_csv(filepath)
header_row = list(df.columns)

# transform
summary_table = df.groupby('Candidate').size().reset_index(name='Total Votes')
summary_table['Proportion'] = (summary_table['Total Votes'] / len(df))

# calculate
total_votes = len(df)
v = summary_table['Total Votes']
winner = summary_table[v.max() == v]['Candidate'].values[0]

# compose output text
output_text = \
f"""
Election Results
---------------------------------------------------
Total Votes: {total_votes}
---------------------------------------------------
{summary_table.to_string()}
---------------------------------------------------
Winner: {winner}
---------------------------------------------------
"""

# output
print(output_text)
output_file = os.path.join(wd,'output.txt')

with open(output_file, 'w') as txt:
    txt.write(output_text)

print('Saved to', output_file)

