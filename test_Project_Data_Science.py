import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'sample_sales_data.csv'
df = pd.read_csv(file_path)

#Display few rows
print(df.head())

#Basic statistics
print(df.info())
print(df.describe())

print(df.isna())
df.fillna(0)

df['Quantity'] = df['Quantity'].astype(int)
df['Price'] = df['Price'].astype(int)
df['Date'] = pd.to_datetime(df['Date']) 

df['Total Sales'] = df['Quantity'] * df['Price']
print(df)
grouped_data = df.groupby('Region')['Total Sales'].sum()

filtered_data = df[df['Quantity']>0]

df.groupby('Region')['Total Sales'].sum().plot(kind='bar')
plt.show()
df.groupby('Category')['Total Sales'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.show()
time = [10,20,30,40]
plt.plot('Sales',time)
