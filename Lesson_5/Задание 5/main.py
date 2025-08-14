import os
import pandas as pd

home_dir = os.path.expanduser("~")
users_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "users_new.csv")
orders_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "orders_new.csv")

users = pd.read_csv(users_path, sep=",")
orders = pd.read_csv(orders_path, sep=",")

order_counts = orders.groupby('user_id')['order_id'].count().reset_index(name='order_count')
filtered = order_counts.query('order_count > 1')
result = filtered.merge(users[['user_id','name']], on='user_id', how='left')[['name','order_count']]
result = result.sort_values(['order_count','name'], ascending=[False, True]).reset_index(drop=True)
print(result.to_string(index=True))