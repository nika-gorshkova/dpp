import pandas as pd

df = pd.read_csv("All_files/customers.csv", sep=",", encoding="utf-8")
df['birth_date'] = pd.to_datetime(df['birth_date'])
filtered = df[(df['gender'] == 'F') & (df['birth_date'].dt.year < 1995)]
print(filtered[['customer_id', 'first_name', 'last_name', 'birth_date']])