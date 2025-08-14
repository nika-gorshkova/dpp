import os
import pandas as pd

home_dir = os.path.expanduser("~")
orders_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "orders.csv")
customers_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "customers.csv")

orders = pd.read_csv(orders_path, sep=",")
customers = pd.read_csv(customers_path, sep=",")

orders['order_date'] = orders['order_date'].str.strip()
orders['order_date'] = pd.to_datetime(orders['order_date'])

orders = orders[(orders['order_date'].dt.year >= 2022) & (orders['order_date'].dt.year <= 2023)]

df = customers.merge(orders, on='customer_id', how='inner')
print(df['gender'].value_counts())