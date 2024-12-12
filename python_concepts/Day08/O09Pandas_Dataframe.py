
import pandas as pd

data = {
 'calories': [450, 375, 290],
 'duration': [60, 45, 35]
}

print(f"data :{data}")

df = pd.DataFrame(data)
print(df)

print("-" * 60)

print(df.loc[0])

print("-" * 60)

print(df.loc[[0, 2]])

print("-" * 60)
df1 = pd.DataFrame(data, index=['day1', 'day2', 'day3'])

print(df1)

print("-" * 60)
print(df1.loc['day2'])
