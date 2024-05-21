import pandas as pd

df = pd.read_csv('heart_statlog_cleveland_hungary_final.csv')

print(df.describe())
print(df.info())
print(df.head(5))


