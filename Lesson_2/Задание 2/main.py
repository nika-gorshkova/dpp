import os
import pandas as pd

home_dir = os.path.expanduser("~")
orders_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "orders.csv")

orders = pd.read_csv(orders_path, sep=",")
orders['order_date'] = orders['order_date'].str.strip()
orders['order_date'] = pd.to_datetime(orders['order_date'])

russian_orders = orders[(orders['customer_id'].between(68, 88)) & (orders['order_date'].dt.year == 2022)]
print(russian_orders[['order_id', 'total']][5:11])