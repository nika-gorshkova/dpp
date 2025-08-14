import os
import pandas as pd

home_dir = os.path.expanduser("~")
users_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "users_new.csv")
orders_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "orders_new.csv")

users = pd.read_csv(users_path, sep=",")
orders = pd.read_csv(orders_path, sep=",")

result = orders.query('product == "C" and price * quantity > 250').copy()
result['total'] = result['price'] * result['quantity']

print(result.to_string(index=True))