import pandas as pd

data = [10, 20, 30]

print(data)

series = pd.Series(data)
print(series)

dataDict = {
    'Name': ['James', 'John', 'Jack'], 
    'Age': [25, 30, 45],
    'City': ["NY", 'LA', 'Chicago']
}
df = pd.DataFrame(dataDict)
print(df)
salary = [200000, 250000, 150000]
df['salary'] = salary
print(df)
df['Age'] = df['Age'] +1
print(df)
df1=df.drop(2)
print(df1)