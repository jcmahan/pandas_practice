import numpy as np
import pandas as pd

np.random.seed(42)
N = 50_000
df = pd.DataFrame({
    "customer_id": np.arange(N),
    "email": [f"user{i}@mail.com" for i in range(N)],
    "age": np.random.randint(18, 75, N).astype(float),
    "income": np.random.normal(60_000, 18_000, N).round(0),
    "signup_src": np.random.choice(["ads", "organic", "referral"], N),
    "orders": np.random.poisson(3, N),
})

def poke_holes(frame):
    # honest NaNs
    frame.loc[frame.sample(frac=0.10).index, "email"] = np.nan
    frame.loc[frame.sample(frac=0.05).index, "age"] = np.nan
    # disguised missing
    frame.loc[frame.sample(frac=0.02).index, "age"] = -1          # sentinel
    frame.loc[frame.sample(frac=0.15).index, "income"] = 0        # default
    frame.loc[frame.sample(frac=0.05).index, "signup_src"] = ""   # empty str
    frame.loc[frame.sample(frac=0.03).index, "signup_src"] = "unknown"
    # meaningful missing: no orders -> no last_order date
    frame["last_order_days_ago"] = np.random.randint(1, 365, N).astype(float)
    frame.loc[frame["orders"] == 0, "last_order_days_ago"] = np.nan
    return frame

df = poke_holes(df)

print(f"shape: {df.shape}")
print(df.head())

print('\nMissing count per column:')
print(df.isna().sum())

print('\nMissing % per column:')
print((df.isna().mean() *100).round(1))

print('\nRows by number of missing fields:')
print(df.isna().sum(axis=1).value_counts().sort_index())

print('\nI doubt signup_src is perfect:')
print(df['signup_src'].value_counts())

print('\nNumeric summary:')
print(df[['age', 'income']].describe().round(0))

df_clean = df.replace({
    'signup_src': {'': np.nan, 'unknown': np.nan}, 
    'age': {-1: np.nan},
    'income': {0: np.nan},
})
print('\nReview post-initial cleaning:')
print((df_clean.isna().mean() *100).round(1))

# create a mailing list so we can contact people via email, but keep the full list separate:
mailing_list = df_clean.dropna(subset=['email'])
print('\nShape of the mailing list DF')
print(mailing_list.shape)

#fill age with the mean of the rows:
df_clean['age'] = df_clean['age'].fillna(df_clean['age'].median())

#replace the nulls in signup_src with not_tracked b/c we don't know where they came from 
df_clean['signup_src'] = df_clean['signup_src'].fillna('not_tracked')

# computing stats for real incomes only
print(f'\nIncome with real values only: ${df_clean['income'].mean():,.0f}')

#last_order_days_ago can give us a count of customers who never ordered by summing the isnas
never_ordered = df_clean['last_order_days_ago'].isna().sum()
print(f'Customers who never ordered: {never_ordered}')

print('final missing percentages:')
print((df_clean.isna().mean() *100).round(1))
