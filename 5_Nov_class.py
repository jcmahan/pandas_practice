import pandas as pd
import numpy as np

#  set the number of records
num_records = 15
rng = np.random.default_rng()
# generate sales data using numpy
sales = rng.integers(100, 2501, size=num_records)

regions = ['north', 'south', 'east', 'west']

products = ['laptop', 'cell phone', 'smart tv', 'tablet']

sales_data = {
    'region': rng.choice(regions, size=num_records),  
    'product': rng.choice(products, size=num_records),
    'sales': sales
}
sales_df = pd.DataFrame(sales_data)
print(sales_data)
print(sales_df.head(10))
  
# find the total of sales from each region
region_df = sales_df.groupby('region')['sales'].sum()
print(f'Group by region: \n{region_df}')
# find the average sales for each product: 
total_product_sales = sales_df.groupby('product')['sales'].mean().round(2)
print(f'Total product sales: \n{total_product_sales}')
# find the total sales for each combination of region and product
total_region_sales = sales_df.groupby(['product', 'region'])['sales'].sum()
print(f'Total region sales: \n{total_region_sales}')
# using ,agg function, to calc sales for each region (group by) 
alt_sales_sum = sales_df.groupby('region').agg(
    total_sales=('sales', 'sum')
).reset_index()
print(f'The alternate way to sum the sales field is: \n{alt_sales_sum}')
# get total average and number of sales in each region
sales_totals = sales_df.groupby('region').agg(
    total_sales=('sales', 'sum'),
    average_sales=('sales', 'mean'),
    sales_count=('sales', 'count')
).reset_index()
sales_totals['average_sales'] = sales_totals['average_sales'].round(2)
print(f'The sales data looks like: \n{sales_totals}')
# reset_index() = after grouping, pandas makes the grouping column into the index. 
# When you want to see the grouping column as a normal column, use .reset_index()
# create a summary of total sales by region (by region = group by region) (total sales = sum of sales)
# make region a normal column instead of an index
summary = sales_df.groupby('region')['sales'].sum().reset_index()
print(f'Using reset index looks like: \n{summary}')
# .apply = to transform a series with a function
# crate a new sales_doubled column by applying a function that doubles each Sales value
sales_df['sales_doubled'] = sales_df['sales'].apply(lambda x: x*2)
print(f'new line with sales doubled: \nn{sales_df}')
# lambda - a short function without a separate def statement. A small function that performs
# one simple anonymous function 
# examples of the same function:
# double = lambda x: x*2
# def double_regular(x):
#     return x*2
# print(double_regular(5))
# create a level column, high if sales >= 1000 else Low 
sales_df['level'] = sales_df['sales'].apply(
    lambda x: 'High' if x >= 1000 else 'Low'  
)
print(f'Adding in the level field looks like: \n{sales_df}')
# data cleaning = str.strip() will remove outer spaces
# import pandas as pd
# names = pd.DataFrame({"Name": [' John ', ' Emma ', ' Jack ']})
# names['clean_name'] = names['Name'].str.strip()
# print(names)
items = pd.DataFrame({'product': ['laptop-pro', 'phone-mini', 'tablet-air']})
items['clean_product'] = items['product'].str.replace('-', ' ')
print(items)