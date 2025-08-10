import pandas as pd

orders = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/orders.csv", sep=",")
orders['order_date'] = orders['order_date'].str.strip()
orders['order_date'] = pd.to_datetime(orders['order_date'])

filtered = orders[(orders['total'].between(30000, 40000)) & (orders['order_date'] >= '2023-01-01')]

print(filtered['order_id'])