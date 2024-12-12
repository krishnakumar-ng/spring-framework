
import pandas as pd

df = pd.read_csv("data.csv")
print(df)

print("-" * 60)

new_df = df.dropna()
print(new_df)

print("-" * 60)
df.dropna(inplace=True)


print("-" * 60)
df = pd.read_csv("data.csv")

nan_rows = df[df.isnull().any(axis=1)]

print(nan_rows)


