import pandas as pd

orders = pd.read_csv("All_Files/orders.csv", sep=",", encoding="utf-8")
orders['order_date'] = orders['order_date'].str.strip()
orders['order_date'] = pd.to_datetime(orders['order_date'])

filtered = orders[(orders['total'].between(10000, 15000)) & (orders['order_date'].dt.year == 2023)]
print(filtered[['order_id', 'total', 'order_date']])