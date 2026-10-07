import pandas as pd
df = pd.read_csv('../data/Sales-Export_2019-2020.csv')

print("Data Shape:", df.shape)

print("Data Types:\n", df.dtypes)

print("First 5 Rows:\n", df.head(5))

print("Missing Values per Column:\n", df.isna().sum())

numeric_columns = ['order_value_EUR', 'cost']
descriptive_statistics = df[numeric_columns].agg(['count', 'mean', 'median', 'min', 'max', 'std'])
print("Descriptive Statistics:\n", descriptive_statistics)

category_statistics = df.groupby('category')['order_value_EUR'].agg(['count','mean','median', 'min', 'max', 'std'])
print("Order Value Stats by Category:\n", category_statistics)

highest_row = df[df['order_value_EUR'] == df['order_value_EUR'].max()]
lowest_row = df[df['order_value_EUR'] == df['order_value_EUR'].min()]
print("Highest Order Value Row:\n", highest_row)
print("Lowest Order Value Row:\n", lowest_row)
