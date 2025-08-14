import os
import pandas as pd

home_dir = os.path.expanduser("~")
orders_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "orders.csv")

orders = pd.read_csv(orders_path, sep=",")
orders['order_date'] = orders['order_date'].str.strip()
orders['order_date'] = pd.to_datetime(orders['order_date'])
filtered = orders[
    (orders['order_date'].dt.year == 2023) &
    (orders['order_date'].dt.month == 2) &
    (orders['total'] > 5000)
]
print(filtered[['order_id', 'total', 'order_date']])