import pandas as pd
import numpy as np

np.random.seed(42)

n = 40

df = pd.DataFrame({
    'name': [f"emp_{i}" for i in range(n)],
    'department': np.random.choice(['Sales', 'Engineering', 'HR', 'Finance'], size=n),
    'age': np.random.randint(22, 60, size=n),
    'salary': np.random.randint(40_000, 225_000, size=n),
    'years_exp': np.random.randint(0,25, size=n)
})
print(df.head())
print(df.shape)
print(df.isna().sum())

print(f'\n{df[df['department'] == "HR"]}')

high_earners = df[df["salary"] > 80000]
print(f'\n{high_earners}')

# AND: Engineers who earn more than 70k
eng_over_70 = df[(df['department']=='Engineering') & (df['salary']>70000)]
# OR: anyone in HR OR Finance
print(f'\nEngineering staff making over 70K/year are\n {eng_over_70}')
hr_or_finance = df[(df['department'] == "HR") | (df['department'] == "Finance")]
print(f'\nStaff in the HR or Finance departments are\n {hr_or_finance}')
# NOT: invert a condition with ~ (tilde) — everyone NOT in Sales
not_salespersons = df[~(df['department'] == "Sales")]
print(f'\nStaff not in sales are: \n{not_salespersons}')

# .isin() replaces long chains of OR conditions.
admin_staff = df[df['department'].isin(['HR', 'Finance'])]
print(f'The Admin staff is \n{admin_staff}')

#.between is a clean way to filter a numbering value(inclusive)
middle_aged = df[df['age'].between(30,40)].sort_values(by='age', ascending=True)
print(f'\nStaff between ages 30 and 40 are: \n{middle_aged}')

#select one row by its index label
print(f'\nindex 2 is:\n{df.loc[2]}')

#select rows 6-11
print(f'\nindices 6-11 are:\n{df.loc[6:11, ['name', 'salary']]}')

#select the name and salary of everyone age > 45

print(f'The names and salary of everyone over 45 years of age is: \n{df.loc[df['age'] > 45, ['name', 'age', 'salary']]}')