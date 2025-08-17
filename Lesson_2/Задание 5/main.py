import pandas as pd

orders = pd.read_csv("All_Files/orders.csv", sep=",", encoding="utf-8")
filtered = orders[(orders['customer_id'].between(10, 20)) & (orders['total'] > 8000)]
print(filtered[['order_id', 'customer_id', 'total']])