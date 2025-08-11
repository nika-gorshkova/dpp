import pandas as pd

users = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/users_new.csv", sep=",")
orders = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/orders_new.csv", sep=",")

orders['total'] = orders['price'] * orders['quantity']
merged = orders.merge(users[['user_id','region']], on='user_id', how='left')
pivot = merged.pivot_table(index='region', columns='product', values='total', aggfunc='sum')
print(pivot)