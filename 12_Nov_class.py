import pandas as pd
import numpy as np

orders = pd.DataFrame({
    'order_id': [101, 102],
    'products': [['laptop', 'mouse', 'charger'], ['tablet', 'LCD screen', 'case']]
})
print(orders)

separate_row = orders.explode('products')

separate_row2 = orders.explode('products', ignore_index=True)

print(separate_row)
print(separate_row2)

orders2 = pd.DataFrame({
    'order_id': [101, 102],
    'products': ['laptop,mouse,charger', 'tablet,LCD screen,case']
})
orders2['products'] = orders2['products'].str.split(',')
print(orders2)
separated = orders2.explode('products', ignore_index=True)
print(separated)

sales = pd.DataFrame(
{   'region': ['East', 'West', 'East', 'South', 'West', 'East'],
    'product': ['laptop', 'phone', 'phone', 'laptop', 'laptop', 'phone'],
    'sales': [1200, 600, 800, 1500, 900, 400]
 }
)

lookup = pd.DataFrame(
    {
        'product': ['laptop', 'phone'],
        'category': ['computers', 'mobiles']
    }
)
result = sales.merge(lookup, on='product', how = 'left')
print(f'this is the Sales df: \n{sales}')
print(f'\nThis is the lookup df: \n{lookup}')
print(f'\nThis is the end result of the merges: \n{result}')