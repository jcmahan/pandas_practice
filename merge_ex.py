import pandas as pd
import numpy as np

np.random.seed(42)
#create the customers table
customers = pd.DataFrame({
    'customer_id': range(1,9),
    'customer_name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
    'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Seattle', 'Denver'], size=8)
})
#create the orders table
orders = pd.DataFrame({
    'order_id': range(101,111), 
    'customer_id': [1,2,2,3,4,5,5,6,6,9],
    'amount': np.random.randint(20, 500, size=10)
})
print('CUSTOMERS:')
print(customers)
print('\nORDERS:')
print(orders)

#inner join
inner = customers.merge(orders, on='customer_id', how='inner')
print('\nINNER JOIN:')
print(inner)

#left join
left = customers.merge(orders, on='customer_id', how='left')
print('\nLEFT JOIN')
print(left)

#right join
right = customers.merge(orders, on='customer_id', how='right')
print('\nRIGHT JOIN')
print(right)

#outer join
outer = customers.merge(orders, on='customer_id', how='outer')
print('\nOUTER JOIN')
print(outer)

#left anti join
left_anti = customers.merge(orders, on='customer_id', how='left_anti')
print('\nLEFT ANTI')
print(left_anti)

#right_anti join
right_anti = customers.merge(orders, on='customer_id', how='right_anti')
print('\nRIGHT ANTI')
print(right_anti)

orders_renamed = orders.rename(columns={'customer_id': 'cust_id'})
rename_merge = customers.merge(orders_renamed, left_on='customer_id', right_on='cust_id')
print('\nRENAMED AND MERGED')
print(orders_renamed)
print(rename_merge)