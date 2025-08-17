import pandas as pd

users = pd.read_csv("All_Files/users_new.csv", sep=",", encoding="utf-8")
orders = pd.read_csv("All_Files/orders_new.csv", sep=",", encoding="utf-8")

orders['total'] = orders['price'] * orders['quantity']
merged = orders.merge(users[['user_id','region']], on='user_id', how='left')
pivot = merged.pivot_table(index='region', columns='product', values='total', aggfunc='sum')
print(pivot)