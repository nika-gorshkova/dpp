import os
import pandas as pd

home_dir = os.path.expanduser("~")
customers_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "customers.csv")

df = pd.read_csv(customers_path, sep=",")
df['birth_date'] = pd.to_datetime(df['birth_date'])
filtered = df[(df['gender'] == 'F') & (df['birth_date'].dt.year < 1995)]
print(filtered[['customer_id', 'first_name', 'last_name', 'birth_date']])