import pandas as pd
import numpy as np

np.random.seed(73)

n = 25

df = pd.DataFrame({
    "rep": np.random.choice(['Alice', 'Betsy', 'Cara', 'Danielle'], size=n), 
    'region': np.random.choice(['East', 'West', 'North', 'South'], size=n),
    'sales': np.random.randint(100, 1000, size=n),
    'deals': np.random.randint(1,20, size=n),
})

df.loc[3,'sales'] = np.nan
df.loc[7, 'sales'] = np.nan
df.loc[21, 'sales'] = np.nan

#print the initial df
print(df)
#sort the df by sales column
print("\n", df.sort_values(by='sales', ascending=False))
#sort the df by sales and region
print("\n", df.sort_values(['region', 'sales'], ascending=[True, False]))
#surface the nas
print('\n', df.sort_values(by='sales', na_position='first'))
#get a new index
print('\n', df.sort_values(by='sales', ascending=False, ignore_index=True))
#show the top 5 values sorted by highest sales value  
print('\n', df.sort_values(by='sales', ascending=False).head(5))