import os
import pandas as pd

home_dir = os.path.expanduser("~")
orders_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "orders.csv")
customers_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "customers.csv")

orders = pd.read_csv(orders_path, sep=",")
customers = pd.read_csv(customers_path, sep=",")

customers['birth_date'] = pd.to_datetime(customers['birth_date'])

merged = orders.merge(customers, on='customer_id', how='inner')
filtered = merged[merged['birth_date'].dt.year == 1990]
print(filtered[['order_id', 'customer_id']])