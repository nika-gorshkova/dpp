import pandas as pd

users = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/users_new.csv", sep=",")
orders = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/orders_new.csv", sep=",")

filt_users = users.query('region == "North" and age < 30')[['user_id', 'name']]
orders_by_filt = orders.merge(filt_users, on='user_id', how='inner')

result = orders_by_filt.groupby('name').size().reset_index(name='order_count')

print(result.to_string(index=True))