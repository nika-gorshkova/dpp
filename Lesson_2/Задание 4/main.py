import pandas as pd

df = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/customers.csv", sep=",")
df['birth_date'] = pd.to_datetime(df['birth_date'])
filtered = df[(df['gender'] == 'F') & (df['birth_date'].dt.year < 1995)]
print(filtered[['customer_id', 'first_name', 'last_name', 'birth_date']])