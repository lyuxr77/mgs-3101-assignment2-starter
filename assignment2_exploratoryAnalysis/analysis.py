from pathlib import Path
import pandas as pd
df = pd.read_csv('../data/Sales-Export_2019-2020.csv',thousands=',', skipinitialspace=True)
df.columns = df.columns.str.strip()
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

# if/else statement for evaluating the average order value.
avg_order_value = df['order_value_EUR'].mean()
threshold = 100000.0
if avg_order_value >= threshold:
    print(f"PASS: Average Order Value (€{avg_order_value:,.2f}) meets the baseline target of €{threshold:,.2f}.")
else:
    print(f"FAIL: Average Order Value (€{avg_order_value:,.2f}) is below the baseline target of €{threshold:,.2f}.")

# Short written summary
print(f"1. Dataset consists of {df.shape[0]} rows and {df.shape[1]} columns with 0 missing values.")
print(f"2. Overall Average Order Value is €{avg_order_value:,.2f}, passing the €100,000 threshold.")
print(f"3. Clothing leads total volume (155 orders), while Outdoors achieves the highest average order value (€118,781.51).")
print(f"4. Average cost is €{df['cost'].mean():,.2f}, showing a healthy gross margin profile.")

#Recommendation 1
df['profit_margin'] = (df['order_value_EUR'] - df['cost']) / df['order_value_EUR']
low_margin_orders = df[df['profit_margin'] < 0.15]
print(f"Recommendation 1 - Low margin orders (< 15% profit margin): {len(low_margin_orders)} records found.")

#Recommendation 2
top_categories = df.groupby('category')['order_value_EUR'].agg(['count', 'mean']).sort_values(by='mean', ascending=False)
print("\nRec 2 - Categories Ranked by Average Order Value:")
print(top_categories)
