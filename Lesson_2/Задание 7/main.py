import pandas as pd

orders = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/orders.csv", sep=",")
customers = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/customers.csv", sep=",")

customers['birth_date'] = pd.to_datetime(customers['birth_date'])

merged = orders.merge(customers, on='customer_id', how='inner')
filtered = merged[merged['birth_date'].dt.year == 1990]
print(filtered[['order_id', 'customer_id']])