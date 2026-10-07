import pandas as pd
df = pd.read_csv('../data/Sales-Export_2019-2020.csv')

print("Data Shape:", df.shape)

print("Data Types:\n", df.dtypes)

print("First 5 Rows:\n", df.head(5))

print("Missing Values per Column:\n", df.isna().sum())
