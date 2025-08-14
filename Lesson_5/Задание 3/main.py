import os
import pandas as pd

home_dir = os.path.expanduser("~")
users_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "users_new.csv")
orders_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "orders_new.csv")

users = pd.read_csv(users_path, sep=",")
orders = pd.read_csv(orders_path, sep=",")

counts = orders['product'].value_counts()
result = counts.rename_axis('product').reset_index(name='order_count')
print(result.to_string(index=True))