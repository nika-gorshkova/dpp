import pandas as pd

orders = pd.read_csv("All_Files/orders.csv", sep=",", encoding="utf-8")
customers = pd.read_csv("All_Files/customers.csv", sep=",", encoding="utf-8")
customers['birth_date'] = pd.to_datetime(customers['birth_date'])
merged = orders.merge(customers, on='customer_id', how='inner')
filtered = merged[merged['birth_date'].dt.year == 1990]
print(filtered[['order_id', 'customer_id']])