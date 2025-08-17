import pandas as pd

users = pd.read_csv("All_Files/users_new.csv", sep=",", encoding="utf-8")
orders = pd.read_csv("All_Files/orders_new.csv", sep=",", encoding="utf-8")

order_counts = orders.groupby('user_id')['order_id'].count().reset_index(name='order_count')
filtered = order_counts.query('order_count > 1')
result = filtered.merge(users[['user_id','name']], on='user_id', how='left')[['name','order_count']]
result = result.sort_values(['order_count','name'], ascending=[False, True]).reset_index(drop=True)
print(result.to_string(index=True))