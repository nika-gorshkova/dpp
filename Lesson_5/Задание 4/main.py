import os
import pandas as pd

home_dir = os.path.expanduser("~")
users_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "users_new.csv")
orders_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "orders_new.csv")

users = pd.read_csv(users_path, sep=",")
orders = pd.read_csv(orders_path, sep=",")

orders['total'] = orders['price'] * orders['quantity']
merged = orders.merge(users[['user_id','region']], on='user_id', how='left')
pivot = merged.pivot_table(index='region', columns='product', values='total', aggfunc='sum')
print(pivot)