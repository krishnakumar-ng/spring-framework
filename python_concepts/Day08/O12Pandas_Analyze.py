
import pandas as pd

df = pd.read_csv("Employee.csv")

print(df)

print("-" * 60)

print(df.head(3))

print("-" * 60)

print(df.tail(3))

print("-" * 60)

print(df.info())
