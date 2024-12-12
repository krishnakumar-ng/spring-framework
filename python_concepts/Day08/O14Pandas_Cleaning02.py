
import pandas as pd

print("-" * 60)

mydf = pd.read_csv("data1.csv")

print(mydf)

print("-" * 60)

# mydf['Date'] = pd.to_datetime(mydf['Date'])
#
# print(mydf)

mydf.loc[7, 'Duration'] = 45

print(mydf)

print("-" * 60)

"""
# to modify a row
for x in mydf.index:
    if mydf.loc[x, "Duration"] > '120':
        mydf.loc[x, "Duration"] = 120

# to drop a row 
for x in mydf.index:
    if mydf.loc[x, "Duration"] > '120':
        mydf.drop(x, inplace=True)
"""
print(mydf.duplicated())
