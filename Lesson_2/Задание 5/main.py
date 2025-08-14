import os
import pandas as pd

home_dir = os.path.expanduser("~")
orders_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "orders.csv")

orders = pd.read_csv(orders_path, sep=",")

filtered = orders[(orders['customer_id'].between(10, 20)) & (orders['total'] > 8000)]
print(filtered[['order_id', 'customer_id', 'total']])