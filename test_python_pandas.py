import pandas as pd

#Create a series
s = pd.Series([1,2,3])
print(s)

#Create a dataframe from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age' : ['10','20','30'],
    'Score': ['21','33','22']
}
df = pd.DataFrame(data)
print(df)

#View first few rows(by default shows first 5 rows)
print(df.head())

#shows last few rows
print(df.tail(2))

#Shape
print(df.shape)

#column names
print(df.columns)

#data types of each column name
print(df.dtypes)

#Summary of the data frame
print(df.info())

#Statistical Summary
print(df.describe())

#select a column
print(df['Name'])

#Selecting multiple columns
print(df[['Name','Age']])

#Selecting rows using .loc (location based indexing)
print(df.loc[1:2])

#Selecting rows using .iloc (integer based indexing)
print(df.iloc[1:2])

#Practice
dataframe = {
    'Product': ['Apples', 'Bananas','Cherries', 'Guava', 'Berries'],
    'Price': ['12','34','56','78','89'],
    'Stock':['11','22','33','44','55']
}


df = pd.DataFrame(dataframe)
df['Price'] = df['Price'].astype(int)
df['Stock'] = df['Stock'].astype(int)


print(df.head(1))
print(df.tail(1))

print(df.columns)
print(df.dtypes)

print(df['Price'])

#Filter rows which have price>50
expensive = df[df['Price'] > 50]
print(expensive)

#Filter rows where stock<30
stock = df[df['Stock']<30]
print(stock)

#Filter rows using multiple conditions
condition = df[(df['Price'] > 30) & (df['Stock'] < 40)]
print(condition)

#Add a new column
df['Value'] = df['Price'] * df['Stock']
print(df)

#Update a column
df['Price'] = df['Price'] + 10
print(df)

#Group by a column and calculate the sum
group_sales = df.groupby('Product')['Stock'].sum()
print(group_sales)

#Group by multiple columns and calculate mean
region_sales =df.groupby(['Product', 'Price'])['Stock'].mean()
print(region_sales)

agg_sales = df.groupby('Product')['Stock'].agg(['sum', 'mean', 'max'])
print(agg_sales)

#New Example

data = {
    'Product': ['Apples', 'Bananas','Cherries', None],
    'Price' : [12,34,None,78],
    'Stock' : [11, None,33, 44]
}

df = pd.DataFrame(data)

#Identify missing values
print(df.isnull())

#Drop rows/columns with missing values
print(df.dropna())

#Fill missing values
df['Price']= df['Price'].fillna(0) #Fill NaN with 0
df['Stock'] = df['Stock'].mean #Fill NAN with mean values
print(df)


#Exercise

data = {
    'Product' :['Socks', 'Shoes', 'Pants', 'Shirts', 'Skirts'],
    'Price' : [20, None, 60, 90, None],
    'Stock' : [22, 12, None, 11, None]
}

df = pd.DataFrame(data)
df['Stock'] = df['Stock'].fillna(df['Stock'].mean())
df['Price']= df['Price'].fillna(df['Price'].mean())
df['Price'] = df['Price'].astype(int)
df['Stock'] = df['Stock'].astype(int)
print(df)
rows = df[df['Price']>20]
print(rows)

df['Value'] = df['Price'] * df['Stock']

df.groupby('Product')['Stock'].sum()

#Advanced Topics 
data1 = {
    'ID' : [1,2,3],
    'Name': ['Alice', 'Bob', 'Charlie']
}
df1 = pd.DataFrame(data1)

data2 = {
    'ID' : [1,2,4],
    'Age' : [25,30,35]
}
df2 = pd.DataFrame(data2)

#Inner merge
merged_inner = pd.merge(df1,df2,on='ID', how='inner')
print(merged_inner)

#Outer merge
outer_merge = pd.merge(df1,df2, on='ID', how='outer')
print(outer_merge)

# Exercise
products = {
    'ProductID': [101, 102, 103, 104],
    'ProductName': ['Laptop', 'Phone', 'Tablet', 'Headphones'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories']
}

df_products = pd.DataFrame(products)

sales = {
    'SaleID': [1, 2, 3, 4, 5],
    'ProductID': [101, 103, 102, 104, 101],
    'Quantity': [2, 1, 3, 1, 5],
    'SaleAmount': [2000, 1200, 1800, 400, 5000]
}

df_sales = pd.DataFrame(sales)

#inner merge
inner_merge = pd.merge(df_products, df_sales, on='ProductID', how='inner')
print(inner_merge)

#outer merge
outer_merge = pd.merge(df_products, df_sales, on='ProductID', how='outer')
print(outer_merge)

#Left Join
left_join = pd.merge(df_sales, df_products, on='ProductID', how='left')
print(left_join)

#Right Join
right_join = pd.merge(df_sales, df_products, on='ProductID', how='right')
print(right_join)


#Numpy and Pandas
import numpy as np
data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Headphones', np.nan],
    'Price': [1000, 500, np.nan, 400, 800],
    'Stock': [50, np.nan, 30, 20, 10]
}

df = pd.DataFrame(data)
print(df)
print(df.isna())
print(df.dropna())
df_filled = df.fillna({'Price': df['Price'].mean(), 'Stock': df['Stock'].mean()})
print(df_filled)
dffill = df.ffill()
print(dffill)

#Exercise
data_employees = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Name': ['John', 'Sara', np.nan, 'Paul', np.nan],
    'Age': [25, 28, np.nan, 35, np.nan],
    'Department': ['HR', 'Finance', 'Marketing', np.nan, 'Finance'],
    'Salary': [50000, 60000, np.nan, 45000, np.nan]
}
df_employees = pd.DataFrame(data_employees)

df_employees['Age'] = df_employees['Age'].fillna(df_employees['Age'].mean())
df_employees['Salary'] = df_employees['Salary'].fillna(df_employees['Salary'].median())
df_employees = df_employees.dropna(subset=['Department'])
df_employees['Name'] = df_employees['Name'].ffill()
df_employees = df_employees.fillna(0)

