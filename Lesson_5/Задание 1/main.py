import os
import pandas as pd

home_dir = os.path.expanduser("~")
users_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "users_new.csv")
orders_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "orders_new.csv")

users = pd.read_csv(users_path, sep=",")
orders = pd.read_csv(orders_path, sep=",")

filt_users = users.query('region == "North" and age < 30')[['user_id', 'name']]
orders_by_filt = orders.merge(filt_users, on='user_id', how='inner')

result = orders_by_filt.groupby('name').size().reset_index(name='order_count')

print(result.to_string(index=True))