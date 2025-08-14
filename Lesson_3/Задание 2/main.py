import os
import pandas as pd

home_dir = os.path.expanduser("~")
orders_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "orders.csv")
customers_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "customers.csv")

orders = pd.read_csv(orders_path, sep=",")
customers = pd.read_csv(customers_path, sep=",")

orders['order_date'] = orders['order_date'].str.strip()
orders['order_date'] = pd.to_datetime(orders['order_date'])

customers['registration_date'] = customers['registration_date'].str.strip()
customers['registration_date'] = pd.to_datetime(customers['registration_date'])

df = customers.merge(orders, on='customer_id', how='left')
df = df.query('registration_date >= "2022-01-01" and order_date.dt.year == 2023 and total > 30000')

print(df[['first_name', 'last_name', 'total']])
print("Количество продаж:", len(df))